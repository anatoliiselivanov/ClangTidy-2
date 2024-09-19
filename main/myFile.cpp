class MyClass
{
public:
    void myFunction();
};

void MyClass::myFunction()
{
    int arr[10] = {0};
    for (int i = 10; i >= 0; i--)
    {
        arr[i] = i;
    }
    // Do something
}