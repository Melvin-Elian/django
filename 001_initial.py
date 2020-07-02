initial=True
dependencies=[

]
operation=[
    migrations.CreateModel(
        name='Destination',
        field=[
            ('id',models.AutoField(auto_created=True,primary_Key=True,serialize=False,verbose_name='ID')),
            ('name',models.CharField(max_length=100)),
            ('img',models.ImageField(upload_to='pics')),
            ('desc',modelsTextField()),
            ('ofter',models.BooleanField(default=False)),
        ],
    ),
]