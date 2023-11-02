#%%
%jsroot
import ROOT
c = ROOT.TCanvas()
f1 = ROOT.TF1("func1", "sin(x)", 0, 10)
f1.Draw()
c.Draw() # Necessary to make the graphics show!"