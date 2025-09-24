class SimpleCalculator
  ALLOWED_OPERATIONS = ['+', '/', '*'].freeze
  class UnsupportedOperation < StandardError
  end

  def self.calculate(first_operand, second_operand, operation)
    if first_operand.is_a?(String) or second_operand.is_a?(String)
      raise ArgumentError.new("Operands are string.")
    end

    case operation
    when nil
      raise UnsupportedOperation.new("No operation found.")

    when "+"
      sum = first_operand + second_operand
      return "#{first_operand} + #{second_operand} = #{sum}"
      
    when "*"
      product = first_operand * second_operand
      return "#{first_operand} * #{second_operand} = #{product}"
      
    when "/"
      begin
        quotient = first_operand / second_operand
      rescue
        return "Division by zero is not allowed."
      end

      return "#{first_operand} / #{second_operand} = #{quotient}"
      
    else
      raise UnsupportedOperation.new("Unsupported Operation.")
    
    end
  end
end