#include<iostream>
#include<cstdlib>

using namespace std;

int merge_sort (int arry[], int temp[], int left, int right);
int merge (int arry[], int temp[], int left, int mid, int right);

int sort(int arry[], int size)
{
	int *temp=(int*)malloc(sizeof(int)*size);
	return merge_sort(arry, temp, 0, size-1);
}

int merge_sort(int arry[], int temp[], int left, int right)
{
	int mid;
	int count=0;

	if(right>left)
	{
		mid=(left+right)/2;
		count=merge_sort(arry, temp, left, mid);
		count +=merge_sort(arry, temp, mid+1, right);
		count +=merge(arry, temp, left, mid+1, right);
	}
	return count;
}

int merge(int arry[], int temp[], int left, int mid, int right)
{
	int left1, mid1, left2;
	int count=0;

	left1=left;
	mid1=mid;
	left2=left;
	
	while((left1<=mid1)&&(mid1<=right))
	{
		if(arry[left1]<arry[mid1])
		{
			temp[left2++]=arry[left1++];
		}
		else
		{
			temp[left2++]=arry[mid1++];
			count=count+(mid-left1);
		}
	}
	while(left1<=mid-1)
	temp[left2++]=arry[left1++];
	while(mid1<=right)
	temp[left2++]=arry[mid1++];
	for(left1=left; left1<=right; left1++)
	{
		arry[left1]=temp[left1];
	}
	return count;
}

int main(int argv, char** args)
{
	int ans;
	int size;
	int arry[size];

	cout<<"How many elements do you want int he array? ";
	cin>>size;
	cout<<"Enter the numbers: "<<endl;
	for(int i=0; i<size;i++)
	{
		cin>>arry[i];
	}
	cout<<"The number of inversions are: ";
	ans=sort(arry,size);
	cout<<ans<<endl;
	return 0;
}
