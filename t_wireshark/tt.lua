do
    -- 定义协议名称和描述
    local myProtocol = Proto("MyProtocol", "Custom Protocol")

    -- 定义协议字段
    local f_field1 = ProtoField.uint8("MyProtocol.field1", "Field 1", base.HEX)
    local f_field2 = ProtoField.uint16("MyProtocol.field2", "Field 2", base.HEX)

    -- 将字段添加到协议
    myProtocol.fields = {f_field1, f_field2}

    -- 获取data解析器
    local data_dissector = Dissector.get("data")

    -- 解析器函数
    local function myProtocol_dissector(buf, pkt, root)
        local buf_len = buf:len()

        -- 根据协议报文格式判断是否为自定义协议
        if buf_len < 3 or buf(0, 1):uint() ~= 0xAA then
            -- 不是自定义协议，调用data解析器
            return data_dissector:call(buf, pkt, root)
        end

        -- 提取字段值
        local field1_value = buf(1, 1):uint()
        local field2_value = buf(2, 2):uint()

        -- 在Packet Details窗口显示协议信息
        local tree = root:add(myProtocol, buf)
        tree:add(f_field1, buf(1, 1)):append_text(", Field 1: " .. field1_value)
        tree:add(f_field2, buf(2, 2)):append_text(", Field 2: " .. field2_value)

        -- 设置Packet List窗口的协议列
        pkt.cols.protocol = "MyProtocol"

        -- 返回true表示成功解析
        return true
    end

    -- 将解析器函数注册到协议解析器
    function myProtocol.dissector(buf, pkt, root)
        myProtocol_dissector(buf, pkt, root)
    end

    -- 将协议解析器添加到udp.port解析器表，监听特定端口
    local udp_table = DissectorTable.get("udp.port")
    udp_table:add(12345, myProtocol)
end