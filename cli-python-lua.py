import os, io
print ('What python-lua features would you like to enable? add = True for this to work properly you can also type all to enable all the features')
pythonluafeatures = input()

if pythonluafeatures == all:
   pythonluafeatures = debug, loadlib, searchers, doloadfile, io, os = True

print (pythonluafeatures + ' enabled')
print ('What lua version would you like python-lua to load?')
os.environ['PYTHON_LUA_VERSION'] = input()
print (os.environ['PYTHON_LUA_VERSION'] + ' loaded')
print ('How would you like to run your lua code?  files or input')
import lua
luarunner = lua.Lua(pythonluafeatures)
runlua = input()
if runlua == "input":

   print ('input your lua code')
   luarunner.run(input())

if runlua == "files":
   print ('Insert the location of your lua file')

filereader = open(input())
luafile = filereader.read()
runluafile = luarunner.run(luafile)
