$().ready(function () {

    $(".container p .add_btn ").click(function () {
        $('#myModal').modal('show');
    })
    $(".keep_btn").click(function () {
        // 关闭模态框
        $('#myModal').modal('hide');
        // 添加节点
        var name = $("#name").val();
        var age = $("#age").val();
        var dep = $("#dep").val();
        // 子节点id 递增
        var id = $(".tbody").children().length + 1
        // console.log(id)
        // 输入校验

        if (name !== "" && age !== "") {
            // 构建tr节点
            var tr = `<tr>
            <td>${id}</td>
            <td>${name}</td>
            <td>${age}</td>
            <td>${dep}</td>
            <td>
            <button class="btn btn-danger btn-sm del_btn">删除</button>
            <button class="btn btn-success btn-sm edit_btn">编辑</button>
            </td>
            </tr>`
        } else {
            alert("用户名和年龄为空!")
        }

        $(".tbody").append(tr);
    })
// 删除节点：事件委派
    $(".tbody").on("click", ".del_btn", function () {
        // console.log($(this).parent().parent())
        $(this).parent().parent().remove();
        // 删除节点后重新排序
        $(".tbody tr td:first-child").each(function (i) {
            $(this).html(i + 1);
        })
    })

// 编辑
    $(".tbody").on("click", ".edit_btn", function () {
        $(this).html("保存").attr("class", "btn btn-warning btn-sm save_btn");
        $(this).parent().siblings().each(function () {
            if ($(this).index() !== 0) {
                var value = $(this).html();
                var input = `<input type="text" value="${value}">`;
                $(this).html("");
                $(this).html(input);
            }
        })
    })

// 保存
    $(".tbody").on("click", ".save_btn", function () {
        $(this).html("编辑").attr("class", "btn btn-success btn-sm edit_btn")
        $(this).parent().siblings().each(function () {
            if ($(this).index() !== 0) {
                var value = $(this).children().val();
                $(this).html(value);
            }
        })
    })
    $(function () {
        $('[data-toggle="popover"]').popover()
    })

})