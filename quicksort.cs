class Program7
{
    //int[] arr = new int[]{ 19, 17, 13, 16, 10 };

    //int[] arr = new int[]{1, 2, 4, 5, 3 };
   int[] arr = new int[]{ 1, 3, 4, 5, 2 };
        //1,2,3,4,5,10


    public void QuickSortImplementation()
    {   
      QuickSort(arr,0,arr.Length-1);

    
    }

    public void QuickSort(int[] arr,int start,int end)
    {
        if(end==0)
        return;


       int pivotIndex = ActuallySort(arr,start,end);

       QuickSort(arr,0,pivotIndex);
       //QuickSort(arr,pivotIndex+1,arr.Length- pivotIndex+1);
        
    }

    public int ActuallySort(int[] arr,int start,int end)
    {
        int pivotIndex= end; //lets take last element    
       //[1,3,6]
        for(int i=0;i< end;i++)
        {
            if(arr[i] > arr[pivotIndex])
            {
                //swap em
                swap(arr,i,pivotIndex);
            }

        }

        return pivotIndex-1 ;



        
    }

    public void swap(int[] arr, int a,int b)
    {
        int temp= arr[a];
        arr[a]=arr[b];
        arr[b]=temp;

    }
}
