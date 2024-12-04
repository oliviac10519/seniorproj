import pandas as pd
import matplotlib.pyplot as plt


def compare_two(dftf1, dftf2):
  win=int(input("What is the exact wording or numbering in the rows of the 'Selling Stage' column that indicates the sale was officially complete?: "))
  lose=int(input("What is the exact wording or numbering in the rows of the 'Selling Stage' column that indicates the opportunity was lost?: "))
  closed_won1=dftf1.loc[(dftf1['Selling Stage'] == win)]
  closed_lost1=dftf1.loc[(dftf1['Selling Stage'] == lose)]
  closed_won2=dftf2.loc[(dftf2['Selling Stage'] == win)]
  closed_lost2=dftf2.loc[(dftf2['Selling Stage'] == lose)]

  print("CLOSED WON FOR 1st TIME FRAME (in count):")
  pivot_won1=pd.pivot_table(closed_won1, index=["Selling Team"], values=["Selling Stage"], aggfunc = 'count')
  print(pivot_won1)

  print("CLOSED WON FOR 2nd TIME FRAME (in count):")
  pivot_won2= pd.pivot_table(closed_won2, index=["Selling Team"], values=["Selling Stage"], aggfunc = 'count')
  print(pivot_won2)

  # merged_df0= pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
  # if (not merged_df0.empty):
  #   sum0=merged_df0.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
  #   sum0.columns=['Timeframe 1', 'Timeframe 2']

  #GRAPHS
  merged_df1= pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
  if (not merged_df1.empty):
    #print("Closed won graph by Selling Team (in USD):")
    # merged_df1= pd.merge(closed_won1, closed_won2, how='outer', on=['Selling Team'])
    sum1=merged_df1.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
    sum1.columns=['Timeframe 1', 'Timeframe 2']
    print()
    print("Closed won by Selling Team (in USD)")
    print(sum1)
    print()
    sum1.plot(kind='bar')
    plt.title("Closed won graph by Selling Team (in USD):")

    #print("Closed won graph by Seller (in USD):")
    merged_df1_1= pd.merge(closed_won1, closed_won2, how='outer', on=['Seller Name'])
    sum1_1=merged_df1_1.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
    sum1_1.columns=['Timeframe 1', 'Timeframe 2']
    print()
    print("Closed won by Seller (in USD)")
    print (sum1_1)
    print()
    sum1_1.plot(kind='bar')
    plt.title("Closed won graph by Seller (in USD):")
  else:
    print("No data to plot for closed won.")

  #......
  print("CLOSED LOST FOR 1st TIME FRAME:")
  pivot_lost1=pd.pivot_table(closed_lost1, index=["Selling Team"], values=["Selling Stage"], aggfunc = 'count')
  print(pivot_lost1)

  print("CLOSED LOST FOR 2nd TIME FRAME:")
  pivot_lost2= pd.pivot_table(closed_lost2, index=["Selling Team"], values=["Selling Stage"], aggfunc = 'count')
  print(pivot_lost2)

  merged_df2= pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
  if(not merged_df2.empty):
    #print("Closed lost graph by Selling Team (in USD): ")
    # merged_df2= pd.merge(closed_lost1, closed_lost2, how='outer', on=['Selling Team'])
    sum2=merged_df2.groupby('Selling Team')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
    sum2.columns=['Timeframe 1', 'Timeframe 2']
    print()
    print("Closed lost by Selling Team (in USD)")
    print (sum2)
    print()
    sum2.plot(kind='bar')
    plt.title("Closed lost graph by Selling Team (in USD):")

    #print("Closed lost graph by Seller (in USD): ")
    merged_df2_2= pd.merge(closed_lost1, closed_lost2, how='outer', on=['Seller Name'])
    sum2_2=merged_df2_2.groupby('Seller Name')[['Recurring ACV (USD)_x', 'Recurring ACV (USD)_y']].sum()
    sum2_2.columns=['Timeframe 1', 'Timeframe 2']
    print()
    print("Closed lost by Seller (in USD)")
    print (sum2_2)
    print()
    sum2_2.plot(kind='bar')
    plt.title("Closed lost graph by Seller (in USD):")

  else:
    print("No data to plot for closed lost.")

  print("Closed won sums: ")
  print()
  print("Total amount of money from deals closed during the 1st timeframe:",  closed_won1['Recurring ACV (USD)'].sum() )
  print("Total amount of money from deals closed during the 2nd timeframe:",  closed_won2['Recurring ACV (USD)'].sum() )

  print()
  print()
  print()

  print('Lost sums: ')
  print()
  print("Total amount of money lost in the 1st timeframe:",  closed_lost1['Recurring ACV (USD)'].sum() )
  print("Total amount of money lost in the 2nd timeframe:",  closed_lost2['Recurring ACV (USD)'].sum() )


  return (pivot_won1) ###can i return 2??

def just_one(dftf1):
  win=int(input("What is the exact wording or numbering in the rows of the 'Selling Stage' column that indicates the sale was officially complete?: "))
  lose=int(input("What is the exact wording or numbering in the rows of the 'Selling Stage' column that indicates the opportunity was lost?: "))


  closed_won1=dftf1.loc[(dftf1['Selling Stage'] == win)]
  closed_lost1=dftf1.loc[(dftf1['Selling Stage'] == lose)]

  print("Total amount of money from deals closed in timeframe:",  closed_won1['Recurring ACV (USD)'].sum() )
  print("Total amount of money lost in the timeframe:",  closed_lost1['Recurring ACV (USD)'].sum() )


  print("CLOSED WON FOR 1st TIME FRAME by Selling Team (count) :")
  pivot_won1=pd.pivot_table(closed_won1, index=["Selling Team"], values=["Selling Stage"], aggfunc = 'count')
  print (pivot_won1)
  if not pivot_won1.empty:
    pivot_won1.plot(kind='bar')
    plt.title("Closed won graph by Selling Team (in count):")
  else:
    print("No data to plot.")

  print("CLOSED WON FOR 1st TIME FRAME by Selling Team (in USD) :")
  pivot_won1=pd.pivot_table(closed_won1, index=["Selling Team"], values=["Recurring ACV (USD)"], aggfunc = 'sum')
  print (pivot_won1)
  if not pivot_won1.empty:
    pivot_won1.plot(kind='bar')
    plt.title("Closed won graph by Selling Team (in USD):")
  else:
    print("No data to plot.")

  print("CLOSED WON FOR THE TIME FRAME by Seller (count) :")
  pivot_won1=pd.pivot_table(closed_won1, index=["Seller Name"], values=["Selling Stage"], aggfunc = 'count')
  print (pivot_won1)
  if not pivot_won1.empty:
    pivot_won1.plot(kind='bar')
    plt.title("Closed won graph by Seller (in count):")
  else:
    print("No data to plot.")

  print("CLOSED WON FOR THE TIME FRAME by Seller (in USD) :")
  pivot_won1=pd.pivot_table(closed_won1, index=["Seller Name"], values=["Recurring ACV (USD)"], aggfunc = 'sum')
  print (pivot_won1)
  if not pivot_won1.empty:
    pivot_won1.plot(kind='bar')
    plt.title("Closed won graph by Selling Team (in USD):")
  else:
    print("No data to plot.")

  print()
  print()
  print("Here are is the closed lost data for you:")

  print("CLOSED LOST FOR THE TIME FRAME by Selling Team (count) :")
  pivot_lost1=pd.pivot_table(closed_lost1, index=["Selling Team"], values=["Selling Stage"], aggfunc = 'count')
  print (pivot_lost1)
  if not pivot_lost1.empty:
    pivot_lost1.plot(kind='bar')
    plt.title("Closed lost graph by Selling Team (in count):")
  else:
    print("No data to plot.")

  print("CLOSED LOST FOR THE TIME FRAME by Selling Team (in USD) :")
  pivot_lost1=pd.pivot_table(closed_lost1, index=["Selling Team"], values=["Recurring ACV (USD)"], aggfunc = 'sum')
  print (pivot_lost1)
  if not pivot_lost1.empty:
    pivot_lost1.plot(kind='bar')
    plt.title("Closed lost graph by Selling Team (in USD):")
  else:
    print("No data to plot.")

  print("CLOSED LOST FOR THE TIME FRAME by Seller (count) :")
  pivot_lost1=pd.pivot_table(closed_lost1, index=["Seller Name"], values=["Selling Stage"], aggfunc = 'count')
  print (pivot_lost1)
  if not pivot_lost1.empty:
    pivot_lost1.plot(kind='bar')
    plt.title("Closed lost graph by Seller (in count):")
  else:
    print("No data to plot.")

  print("CLOSED LOST FOR THE TIME FRAME by Seller (in USD) :")
  pivot_lost1=pd.pivot_table(closed_lost1, index=["Seller Name"], values=["Recurring ACV (USD)"], aggfunc = 'sum')
  print (pivot_lost1)
  if not pivot_lost1.empty:
    pivot_lost1.plot(kind='bar')
    plt.title("Closed lost graph by Seller(in USD):")
  else:
    print("No data to plot.")


  return(pivot_won1)
