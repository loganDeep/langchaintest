class Program7
{
    //int[] arr = new int[]{ 19, 17, 13, 16, 10 };

    //int[] arr = new int[]{1, 2, 4, 5, 3 };
   //int[] arr = new int[]{ 1, 3, 4, 5, 2 };
   //int[] arr = new int[]{ 5, 1, 3, 2, 4 };
   //int[] arr = new int[]{ 10, 7, 9, 3, 2, 8, 5, 6, 1, 4 };
  int[] arr = new int[]{ 100, 3, 5, 101, 8, 6, 1, 9, 7, 4, 12, 99 };
  // int[] arr = new int[]{ 5, 1, 8, 7, 3, 2, 6, 4 };

    public void QuickSortImplementation()
    {   
      QuickSort2(arr,0,arr.Length-1);

      foreach(var s in arr)
      Console.WriteLine($"{s}\n");
    }

    public void QuickSort2(int[] arr,int start,int end)
    {
        if(end==0)
        return;


       int pivotIndex = ActuallySort(arr,start,end);

       QuickSort2(arr,0,pivotIndex);
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
