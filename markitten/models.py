# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApplicationCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_category'
        unique_together = (('slug', 'parent'),)


class ApplicationComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ApplicationProduct', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'application_comment'


class ApplicationProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    reorder_level = models.IntegerField()
    carousel_image_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_2 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_3 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_2 = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(ApplicationCategory, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'application_product'


class ApplicationProductarchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    carousel_image_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_2 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_3 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_2 = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(ApplicationCategory, models.DO_NOTHING, blank=True, null=True)
    discount = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'application_productarchive'


class ApplicationSupplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    supplier_address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_supplier'


class ApplicationSupplierarchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    supplier_address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_supplierarchive'


class ApplicationSupplierproduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_time = models.DurationField(blank=True, null=True)
    product = models.ForeignKey(ApplicationProduct, models.DO_NOTHING)
    supplier = models.ForeignKey(ApplicationSupplier, models.DO_NOTHING)
    supplier_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'application_supplierproduct'


class ApplicationUserDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'application_user_details'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MarkittenAppCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markitten_app_category'
        unique_together = (('slug', 'parent'),)


class MarkittenAppComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rating = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('MarkittenAppProduct', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'markitten_app_comment'


class MarkittenAppComplaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    imagereview = models.CharField(db_column='imageReview', max_length=100)  # Field name made lowercase.
    product = models.ForeignKey('MarkittenAppProduct', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'markitten_app_complaint'


class MarkittenAppProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    carousel_image_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_2 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_3 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_2 = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(MarkittenAppCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markitten_app_product'


class MarkittenAppProductarchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    carousel_image_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_2 = models.CharField(max_length=100, blank=True, null=True)
    carousel_image_3 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_1 = models.CharField(max_length=100, blank=True, null=True)
    carousel_video_2 = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(MarkittenAppCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markitten_app_productarchive'


class MarkittenAppProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    sex = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    is_subscribed = models.BooleanField()
    landline_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    office_address = models.CharField(max_length=100)
    office_number = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    present_address = models.CharField(max_length=100)
    shopping_address = models.CharField(max_length=100)
    birthday = models.DateField()
    office_email = models.CharField(max_length=100)
    personal_email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'markitten_app_profile'


class MarkittenAppReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rating = models.IntegerField(blank=True, null=True)
    imagereview = models.CharField(db_column='imageReview', max_length=100)  # Field name made lowercase.
    product = models.ForeignKey(MarkittenAppProduct, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'markitten_app_review'


class MarkittenAppSupplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    supplier_address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markitten_app_supplier'


class MarkittenAppSupplierarchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    supplier_address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markitten_app_supplierarchive'


class MarkittenAppSupplierproduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_price = models.DecimalField(max_digits=8, decimal_places=2)
    lead_time = models.DurationField(blank=True, null=True)
    product = models.ForeignKey(MarkittenAppProduct, models.DO_NOTHING)
    supplier = models.ForeignKey(MarkittenAppSupplier, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'markitten_app_supplierproduct'
