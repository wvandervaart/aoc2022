#!/usr/bin/env ruby
dirs = []
#dirs.default_proc = proc { |h, k| h[k] = 0 }

file='input.txt'
File.readlines(file).each do |line|
  case line.split()
  when '$', 'cd', '/'
    c = ['']
  when '$', 'cd', '..'
    c.pop()
  when '$', 'cd', x
    c.append(x)
  when '$', 'ls'
    pass
  when 'dir', _
    pass
  when s, _
        for d in c.reduce(0)
            dirs[d] += int(s)
        end
  puts line
  end
end
#tot = 0
#for v in dirs.values():
#    if v <= 100_000:
#        print(v)
#        tot += v
#print(tot)