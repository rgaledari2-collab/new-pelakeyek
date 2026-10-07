import xml.sax.saxutils as saxutils

def escape(val):
    if val is None:
        return ""
    return saxutils.escape(str(val))

xml = """<?xml version="1.0" encoding="UTF-8"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:html="http://www.w3.org/TR/REC-html40">
 <Styles>
  <Style ss:ID="Default" ss:Name="Normal">
   <Alignment ss:Vertical="Center"/>
   <Borders/>
   <Font ss:FontName="Tahoma" x:CharSet="178" ss:Size="10"/>
   <Interior/>
   <NumberFormat/>
   <Protection/>
  </Style>
  <Style ss:ID="Header">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#000000"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#000000"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#000000"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#000000"/>
   </Borders>
   <Font ss:FontName="Tahoma" x:CharSet="178" ss:Size="11" ss:Bold="1" ss:Color="#FFFFFF"/>
   <Interior ss:Color="#1B4D3E" ss:Pattern="Solid"/>
  </Style>
  <Style ss:ID="Cell">
   <Alignment ss:Horizontal="Right" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
   </Borders>
   <Font ss:FontName="Tahoma" x:CharSet="178" ss:Size="10"/>
  </Style>
  <Style ss:ID="CellCenter">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#D1D5DB"/>
   </Borders>
   <Font ss:FontName="Tahoma" x:CharSet="178" ss:Size="10"/>
  </Style>
 </Styles>
 <Worksheet ss:Name="خلاصه ۱۹ روستا" ss:RightToLeft="1">
  <Table>
   <Row ss:StyleID="Header">
    <Cell><Data ss:Type="String">ردیف</Data></Cell>
    <Cell><Data ss:Type="String">نام روستا</Data></Cell>
    <Cell><Data ss:Type="String">وضعیت شناسنامه</Data></Cell>
    <Cell><Data ss:Type="String">جمعیت</Data></Cell>
    <Cell><Data ss:Type="String">خانوار</Data></Cell>
   </Row>
   <Row ss:StyleID="Cell">
    <Cell ss:StyleID="CellCenter"><Data ss:Type="Number">1</Data></Cell>
    <Cell><Data ss:Type="String">سوره</Data></Cell>
    <Cell><Data ss:Type="String">ثبت کامل</Data></Cell>
    <Cell ss:StyleID="CellCenter"><Data ss:Type="String">۴,۱۷۵</Data></Cell>
    <Cell ss:StyleID="CellCenter"><Data ss:Type="String">۱,۰۵۱</Data></Cell>
   </Row>
  </Table>
 </Worksheet>
</Workbook>
"""

with open("/tmp/test.xls", "w", encoding="utf-8") as f:
    f.write(xml)

print("Generated test.xls, bytes:", len(xml))
