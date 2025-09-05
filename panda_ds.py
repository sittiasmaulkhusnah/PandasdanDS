# Import Library
import pandas as pd
import numpy as np
import re      #untuk regex saat filter string


#1. menampilkan array 1 dimensi
ds=pd.Series([2,4,6,8,10])
print(ds)

#2.
data=pd.Series(["a","b","c"])
np1=np.array(["x","y","z"])
data_np=pd.Series(np1)

print(data)
print(data_np)

# mengatur indeks pada numpy array data-np di atas
data_np=pd.Series(np1, index=[2,3,4])
print(data_np)

#3. operasi
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
dsa=ds1+ds2 
dsb=ds1-ds2
dsc=ds1*ds2
dsd=ds1/ds2
print(dsa)
print(dsb)
print(dsc)
print(dsd)

#4. convert pandas modul series ke python list
ds=pd.Series([2,4,6,8,10])
print("Pandas Series Type")
print(ds)
print(type(ds))

print("Convert Pandas Series ke Python list")
print(ds.tolist())
print(type(ds.tolist()))

#5. convert Numpy array ke Pandas Series
np_array=np.array([0, 20, 30, 40, 50])
print("NumPy array:")
print(np_array)

new_np=pd.Series(np_array)
print("konversi Pandas series")
print(new_np)

#6. generate angka random
num_state=np.random.RandomState(100)
num_series=pd.Series(num_state.normal(10,4,20))

print(num_series)
print(num_state)

# Load Data
#7.1. load data dari folder yang sama dengan coding
df=pd.read_csv("penjualan.csv")
print(df.head())

#8. menampilkan tabel penjualan februari
df=pd.read_csv("penjualan.csv")

print(df["feb"].head())

#9. menampilkan lebih dari satu kolom (series), gunakan double bracket [[]]
df=pd.read_csv("penjualan.csv")
print(df[["feb", "mar"]].head(3))

#10. tambah kolom teks berisi angka
#10.1. 
penjual=["penjual no"+str(i)for i in range(1,11)]
print(penjual)

#10.2.
df["urutan"]=penjual
print(df)

#11. ekstraksi angka dari teks 
df["no"]=df["urutan"].str.extract(r"(\d+)").astype("int64")
print(df)

# memilih data berdasarkan bari dan kolom
#12. menampilkan hanya kolom tertentu
#12.1. menampilkan baris dengan indeks berlabel 0
print(df.loc[0])
print(df.iloc[0])
print(df[:1])

#12.2. menampilkan baris indeks berlabel 0 dan kolom berlaber jan
print(df.loc[0,"jan"])
print(df.iloc[0,1])

print(df[["jan"]][:1])

#12.3. menampilkan baris berlabel 0 sampai 2 dan kolom nama, jan, mar
print(df.loc[0:2, ["nama", "jan", "mar"]])

#12.3. menampilkan baris 0-3, kolom 0 (nama), 1(jan), 3 (mar)
print(df.iloc[0:3, [0,1,3]])

#12.4 menampilkan semua baris pada kolom **nama** dan **apr**
print(df.loc[:, ["nama", "apr"]])
print(df.iloc[:, [0,4]])
print(df[["nama", "apr"]])

#12.5. menampilkan semua baris pada kolom nama sampai feb
print(df.loc[:, ["nama", "feb"]])
print(df.iloc[:, :3])
print(df[["nama", "jan", "feb"]])

# menampilkan semua baris dan semua kolom
print(df.loc[:, :])

# Memfilter Data
#13. memilih berdasarkan satu kondisi
import re

#13.1. memilih angka 
# sama dengan
print(df[df["jan"]==200])
df[df.jan.eq(200)]

# tidak sama dengan
print(df[df["jan"]!=200])
df[df.jan.ne(200)]
print(df[~(df["jan"]==20)])

# angka lebih dari
print(df[df["jan"]>200])
df[df.jan.gt(200)]

# lebih dari satu atau sama dengan
print(df[df["jan"]>=200])
df[df.jan.ge(200)]

# kurang dari
print(df[df["jan"]<200])
df[df.jan.lt(200)]

# kurang dari atau sama dengan
print(df[df["jan"]<=200])
df[df.jan.le(200)]

#13.2. memilih teks
print(df[df["nama"].str.contains("andi")])
print(df[df["nama"].str.contains("jul")])

# abaikan huruf kecil
df[df["nama"].str.contains("in")]

print(df[df["nama"].str.contains("in",flags=re.IGNORECASE)])

# memilih data yang berada di list atau dataframe lain
# menampilka kolom februari pada file
feb_penjualan=[130,220]
print(df[df["feb"].isin(feb_penjualan)])

#14. membuat kategori tinggi dan rendah
d={"tinggi":[320,300],"rendah":[95,100]}
df1=pd.DataFrame(data=d)
print(df1)

print(df[df["jan"].isin(df1["tinggi"])])
print(df[df["jan"].isin(df1["rendah"])])

#memilih lebih dari satu kondisi
# memilih diantara dua rentang nilai
print(df[(df["jan"]>100)&(df["jan"]<300)])

print(df[(df["nama"].str.contains("on",flags=re.IGNORECASE))|(df["jan"]>200)])
print(df.describe())

# Metode metode pandas
#15. metode apply untuk menjalankan fungsi pada setiap baris pada data series
data=[1,2,3,5,8,13,21]
d_int=pd.Series(data)
def kecilbesar(num):
    if num <3:
        return "kecil"    
    elif num >=3 and num <13:
        return "sedang"
    else:
        return "besar"
    
print(d_int.apply(kecilbesar))

# info DataFrame
print(df.info())






