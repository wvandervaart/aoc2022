class Directory
    attr_accessor :data, :name, :children, :parent
  
    def initialize(name, data: 0, children: {}, parent: nil)
      @name = name
      @data = data
      @children = children
      @parent = parent
    end
  end
  
  @sizes = {}
  
  def calculate_dir_size(input)
    tree = build_tree(input)
    add_sizes(tree.children)
    @sizes
  end
  
  def add_sizes(children)
    children.map do |k, v|
      @sizes[k] = v.data + add_sizes(v.children)
    end.sum
  end
  
  def build_tree(input, key: '__')
    current_dir = Directory.new('_')
    root = current_dir
  
    input.split("\n").each do |line|
      case line
      when '$ cd /'
        current_dir.children[current_dir.name + '_'] = Directory.new(current_dir.name + '_', parent: current_dir)
      when '$ cd ..'
        current_dir = current_dir.parent
      when /\$ cd (.+)/
        key = $1
        current_dir = current_dir.children[current_dir.name + key]
      when '$ ls' 
      when /(\d+) .+/
        current_dir.data += $1.to_i
      when /dir (.+)/
        key = $1
        current_dir.children[current_dir.name + key] = Directory.new(current_dir.name + key, parent: current_dir)
      end
    end
    root
  end
  
  input = File.read('./input.txt')
  
  puts output = calculate_dir_size(input)
  puts output.values.select { |v| v <= 100000 }.sum
  puts output.values.max
  