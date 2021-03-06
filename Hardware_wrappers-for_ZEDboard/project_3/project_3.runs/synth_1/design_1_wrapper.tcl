# 
# Synthesis run script generated by Vivado
# 

  set_param gui.test TreeTableDev
set_msg_config -id {HDL 9-1061} -limit 100000
set_msg_config -id {HDL 9-1654} -limit 100000
create_project -in_memory -part xc7z020clg484-1
set_property target_language VHDL [current_project]
set_property board_part em.avnet.com:zed:part0:1.0 [current_project]
set_param project.compositeFile.enableAutoGeneration 0
set_property default_lib xil_defaultlib [current_project]

add_files C:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/design_1.bd
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_1/design_1_processing_system7_0_1.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_axi_gpio_0_1/design_1_axi_gpio_0_1_ooc.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_axi_gpio_0_1/design_1_axi_gpio_0_1.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_axi_gpio_0_1/design_1_axi_gpio_0_1_board.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_axi_gpio_1_0/design_1_axi_gpio_1_0_ooc.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_axi_gpio_1_0/design_1_axi_gpio_1_0.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_axi_gpio_1_0/design_1_axi_gpio_1_0_board.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_rst_processing_system7_0_100M_1/design_1_rst_processing_system7_0_100M_1.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_rst_processing_system7_0_100M_1/design_1_rst_processing_system7_0_100M_1_ooc.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_rst_processing_system7_0_100M_1/design_1_rst_processing_system7_0_100M_1_board.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_xbar_1/design_1_xbar_1_ooc.xdc]
set_property used_in_implementation false [get_files -all c:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/ip/design_1_auto_pc_0/design_1_auto_pc_0_ooc.xdc]
set_property used_in_implementation false [get_files -all C:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/design_1_ooc.xdc]
set_msg_config -id {IP_Flow 19-2162} -severity warning -new_severity info
set_property is_locked true [get_files C:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/design_1.bd]

read_vhdl -library xil_defaultlib C:/Users/dwijsukesh.ks/project_3/project_3.srcs/sources_1/bd/design_1/hdl/design_1_wrapper.vhd
read_xdc dont_touch.xdc
set_property used_in_implementation false [get_files dont_touch.xdc]
set_param synth.vivado.isSynthRun true
set_property webtalk.parent_dir C:/Users/dwijsukesh.ks/project_3/project_3.cache/wt [current_project]
set_property parent.project_dir C:/Users/dwijsukesh.ks/project_3 [current_project]
catch { write_hwdef -file design_1_wrapper.hwdef }
synth_design -top design_1_wrapper -part xc7z020clg484-1
write_checkpoint design_1_wrapper.dcp
report_utilization -file design_1_wrapper_utilization_synth.rpt -pb design_1_wrapper_utilization_synth.pb
