#include <iostream>
#include <string>
using namespace std;

int main()
{
//variables declared
	int fund[4], con,clas=0,mc=0,i;
	string classtr[] ={"freshman","sophomores","juniors","seniors"};
    cout << fund[1] << endl;
	//code to get continuous input untill class is 999
	while(clas!=999)
	{
		//get the user class input
        cout<<" 1.freshmen \n 2.sophomores \n 3.juniors \n 4.seniors "<<endl;
        cout<<"Enter your class:";
        cin>>clas;
        if(clas!=999)
        {
        	//get the contrubution amount
        	cout<<"Enter your contribution amount$: "<<endl;
        	cin>>con;
        	//calculate the contribution total for each class
        	if (clas==1)
        	{
        		fund[0]=fund[0]+con;
        		con=0;
        	}
        	else if (clas==2)
        	{
        		fund[1]=fund[1]+con;
        		con=0;
        	}
        	else if (clas==3)
        	{
        		fund[2]=fund[2]+con;
        		con=0;
        	}
        	else if(clas==4)
        	{
        		fund[3]=fund[3]+con;
        		con=0;
        	}
          }
        }
        	//calculate the max contribution fund and class
        	int max=fund[0];
        	for (i=1;i<4;i++)
        	{
        		if(max<fund[i])
        		{
        			max=fund[i];
        			mc=i;
        		}
        	}
        	cout<<"The class and the collected fund:"<<endl;
        	for (i=0;i< 4;i++)
        	{
        cout<<classtr[i]<<"colects $"<<fund[i]<<endl;
        	}
        	cout<<"The maximum fund collected class is"<<classtr[mc]<<" and collected fund is $ "<<fund[mc]<<endl;
        	system("pause");
	return 0;
}
