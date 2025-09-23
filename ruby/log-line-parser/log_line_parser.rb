class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    index = @line.index(':')
    @line[index + 1..].strip
  end

  def log_level
    data = @line.match(/\[(\w+)\]/)
    data[1].downcase
  end

  def reformat
    data = @line.match(/\[(\w+)\]:\s*(.*)/)
    log_level = data[1].downcase
    msg = data[2].strip
    "#{msg} (#{log_level})"
  end
end
