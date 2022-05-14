import numpy as np
import pandas as pd
import xlsxwriter
exdzi=np.array(([20,"strVeri","strVeri"],[14,"strVeri","strVeri"],[17,"strVeri","strVeri"]))
exdos=pd.DataFrame(exdzi,index=["ZEHRA","ALİ OSMAN","YUNUS EMRE "], columns=["strVeri","strVeri","strVeri"])
print(exdos)

dosyalinki=exdos.to_excel("dosya yolu",sheet_name="sayfa1")
print(dosyalinki)

aiçeaktar=pd.read_excel("dosya yolu",sheet_name="sayfa1")
print(aiçeaktar)

