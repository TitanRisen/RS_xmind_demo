import xmind
from xmind.core.const import TOPIC_DETACHED
from xmind.core.markerref import MarkerId
from xmind.core.topic import TopicElement


def gen_my_xmind_file(name, post_form, form_items ):

    file_path = "./" + name + ".xmind"
    workbook = xmind.load(file_path)
    # get the first sheet(a new workbook has a blank sheet by default)
    sheet1 = workbook.getPrimarySheet()
    # design_sheet1(sheet1, name, number , address, flow)
    design_sheet2(sheet1, name, post_form, form_items)

    try:
        xmind.save(workbook, path=file_path)
        return True
    except Exception:
        return False


def design_sheet1(sheet1, name, number , address, flow):
    # ***** first sheet *****
    sheet1.setTitle(name)  # set its title

    # get the root topic of this sheet(a sheet has  a blank root topic by default)
    root_topic1 = sheet1.getRootTopic()
    root_topic1.setTitle(name)  # set its title

    # detached_topic1.setPosition(0, 30)

    # create some sub topic element
    sub_topic1 = root_topic1.addSubTopic()
    sub_topic1.setTitle("姓名")
    sub_topic1_1 = sub_topic1.addSubTopic()
    sub_topic1_1.setTitle(name)

    sub_topic2 = root_topic1.addSubTopic()
    sub_topic2.setTitle("电话")
    sub_topic2_1 = sub_topic2.addSubTopic()
    sub_topic2_1.setTitle(number)

    sub_topic3 = root_topic1.addSubTopic()
    sub_topic3.setTitle("地址")
    sub_topic3_1 = sub_topic3.addSubTopic()
    sub_topic3_1.setTitle(address)

    sub_topic4 = root_topic1.addSubTopic()
    sub_topic4.setTitle("办理流程")
    sub_topic4_1 = sub_topic4.addSubTopic()
    sub_topic4_1.setTitle(flow)
    

    # create a detached topic(attention: only root topic can add a detached topic)
    

    

def design_sheet2(sheet1, name, post_form, form_items=None):
    # ***** first sheet *****
    sheet1.setTitle(name)  # set its title

    # get the root topic of this sheet(a sheet has  a blank root topic by default)
    root_topic1 = sheet1.getRootTopic()
    root_topic1.setTitle(name)  # set its title

    # create some sub topic element
    for item in form_items:
        print(item)
        sub_topic1 = root_topic1.addSubTopic()
        sub_topic1.setTitle(item["name"])
        sub_topic1_1 = sub_topic1.addSubTopic()
        sub_topic1_1.setTitle(post_form[item["id"]])


    # create a detached topic(attention: only root topic can add a detached topic)




if __name__ == '__main__':
    gen_my_xmind_file()