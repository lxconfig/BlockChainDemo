import re


"""
    贪婪模式：在表达式匹配成功的前提下，尽可能多的匹配

    非贪婪模式：在表达式匹配成功的前提下，尽可能少的匹配
        - .*? 实现非贪婪模式
"""

def main():
    """
        从html中提取文字信息
    """
    html = """
    <dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
            <p>岗位职责：</p>
            <p>1、&nbsp; 主要参与“短书“项目的服务端开发；</p>
            <p>2、&nbsp; 根据产品的需求提供符合项目或产品的解决方案；</p>
            <p>3、&nbsp; 参与平台日常开发，包括但不限于程序设计审查、代码审查等工作；</p>
            <p>4、&nbsp; 编写程序设计、API等相关技术文档。</p>
            <p><br></p>
            <p>岗位要求：</p>
            <p>1、本科学历，2年Python相关工作经验，熟练使用Python语言;</p>
            <p>2、熟悉Linux常用命令或有Mac下的开发经验，能在常见Linux服务器（CentOS/Ubuntu）上简单排查问题；</p>
            <p>3、熟练使用MySQL/Postgres，了解NoSQL；</p>
            <p>4、熟悉Nginx/Apache等Web服务器的配置；</p>
            <p>5、有良好的需求分析、设计能力、规范的编程风格和良好文档习惯；</p>
            <p>6、至少精通一种Python框架（Django/Tornado）。</p>
            <p><br></p>
            <p>加分项</p>
            <p>1、有写 Blog 的习惯，活跃技术社区，参与开源项目等；</p>
            <p>2、有代码洁癖，对代码精益求精，对技术有极客热情。</p>
            <p><br></p>
            <p>我们的研发中心成员经过严格筛选，只为缔造一个志同道合，合作无间的团队。如果你觉得渴望在团队里面一起做点事情，那加入我们，试着一起创造出伟大的产品。</p>
        </div>
    </dd>"""

    text = re.sub(r"<.*?>", "", html)

    print(text)




if __name__ == "__main__":
    main()