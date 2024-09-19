class MyClass
{
public:
    void myFunction();
};

void MyClass::myFunction()
{
    int arr[10] = {0};
    for (int j = 10; j >= 0; j--)
    {
        arr[j] = j;
    }
    // Do something
}