import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_1(fileName):
    print("Plotting Plot 1............")
    data = pd.read_csv(fileName, header=None,index_col=False)
    data.loc[len(data)] = data.columns
    f, ax = plt.subplots(4,4)
    i = 0
    while i < len(data)-1:
      plt.sca(ax[i//4,i%4])
      ax[i//4,i%4].set_xlabel("Key Bytes")
      ax[i//4,i%4].set_ylabel("Correlation")
      for x in data.iloc[len(data)-1]:
        if data.iloc[i,int(x)] == data.max(axis=1).iloc[i]:
          ax[i//4,i%4].scatter(x, data.iloc[i,int(x)], color='red')
          ax[i//4,i%4].text(x-5, data.iloc[i,int(x)]-0.04, str(hex(int(x))), fontdict=None)
        else:
          ax[i//4,i%4].scatter(x, data.iloc[i,int(x)], color='black')
      if i == 0:
        ax[i//4,i%4].set_title("1st byte of key")
      elif i == 1:
        ax[i//4,i%4].set_title("2nd byte of key")
      elif i == 2:
        ax[i//4,i%4].set_title("3rd byte of key")
      else:
        ax[i//4,i%4].set_title(str(i+1)+"th byte of key")
      plt.tight_layout()
      fig = ax[i//4,i%4].get_figure()
      fig.set_size_inches(20, 12)
      i+=1
      print(i, "byte plotted for Plot 1...")
    print("Done Exporting Plot 1")
    fig.savefig("plot1.png")


def plot_2(fileName):
    print("Plotting Plot 2............")
    data = pd.read_csv(fileName, header=None, index_col=False)
    data.loc[len(data)] = data.columns
    f, ax = plt.subplots(4, 4)
    i = 0
    last_y_col = 100
    noOfBytes =1;
    while i < len(data) - 1:
        x_col = i // 40
        y_col = (i - 40 * (i // 40)) // 10
        if last_y_col != y_col:
            plt.sca(ax[x_col, y_col])
            ax[x_col, y_col].set_xlabel("No of traces")
            ax[x_col, y_col].set_ylabel("Correlation")
            byteNo = i//10
            if byteNo == 0:
                ax[x_col, y_col].set_title("1st byte of key")
            elif byteNo == 1:
                ax[x_col, y_col].set_title("2nd byte of key")
            elif byteNo == 2:
                ax[x_col, y_col].set_title("3rd byte of key")
            else:
                ax[x_col, y_col].set_title(str(byteNo+1)+"th byte of key")
        for x in data.iloc[len(data) - 1]:
            if data.iloc[i, int(x)] == data.max(axis=1).iloc[i]:
                ax[x_col, y_col].scatter(((i % 10) + 1) * 10, data.iloc[i, int(x)], color='red')
                if ((i % 10) + 1) * 10 == 100:
                    ax[x_col, y_col].text(x, data.iloc[i, int(x)] + 0.2, str(hex(int(x))), fontdict=None)
                    print(noOfBytes, "byte plotted for Plot 2...")
                    noOfBytes+=1
                    
            else:
                ax[x_col, y_col].scatter(((i % 10) + 1) * 10, data.iloc[i, int(x)], color='black')
        last_y_col = y_col
        i += 1
        plt.tight_layout()
        fig = ax[x_col, y_col].get_figure()
        fig.set_size_inches(20, 12)
    print("Done Exporting Plot 2")
    fig.savefig("plot2.png")

if __name__ == '__main__':
    plot_1("plot1Data.csv")
    plot_2("plot2Data.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
