module Jekyll
  module TypeFilter
    def type(input)
      case input.class.to_s
        when 'String'.freeze then 'string'.freeze
        when 'Float'.freeze, 'Fixnum'.freeze then 'number'.freeze
        when 'TrueClass'.freeze, 'FalseClass'.freeze then 'boolean'.freeze
        when 'Array'.freeze then 'array'.freeze
        when 'Hash'.freeze then 'hash'.freeze
        when 'NilClass'.freeze then 'nil'.freeze
        else raise 'Unhandled type: "' + input.class.to_s + '"'
      end
    end

    def is_string(input)
        type(input) == 'string'
    end

    def is_number(input)
        type(input) == 'number'
    end

    def is_boolean(input)
        type(input) == 'boolean'
    end

    def is_true(input)
        input.is_a? TrueClass
    end

    def is_false(input)
        input.is_a? TrueClass
    end

    def is_array(input)
        type(input) == 'array'
    end

    def is_hash(input)
        type(input) == 'hash'
    end

    def is_nil(input)
        type(input) == 'nil'
    end
  end
end


Liquid::Template.register_filter(Jekyll::TypeFilter)
