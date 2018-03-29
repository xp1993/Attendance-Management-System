$(function () {/* 文档加载，执行一个函数*/
    console.log("dasdasdsadsa")
    $('#defaultForm')
        .bootstrapValidator({
            message: 'This value is not valid',
            feedbackIcons: {
                /*input状态样式图片*/
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                /*验证：规则*/
                username: {//验证input项：验证规则
                    message: 'The username is not valid',

                    validators: {
                        notEmpty: {//非空验证：提示消息
                            message: '用户名不能为空'

                        },
                        stringLength: {
                            min: 1,
                            max: 20,
                            message: '用户名长度必须在1到20之间'
                        },
                        threshold: 1, //有1字符以上才发送ajax请求，（input中输入一个字符，插件会向服务器发送一次，设置限制，1字符以上才开始）
                        remote: {//ajax验证。server result:{"valid",true or false} 向服务发送当前input name值，获得一个json数据。例表示正确：{"valid",true}
                            url: '/register/',//验证地址
                            message: '用户已存在',//提示消息
                            delay: 2000,//每输入一个字符，就发ajax请求，服务器压力还是太大，设置2秒发送一次ajax（默认输入一个字符，提交一次，服务器压力太大）
                            type: 'POST',//请求方式
                            /**自定义提交数据，默认值提交当前input value*/
                            data: function(t) {

                               return {
                                   stu_num_verify: $('[name="stu_num"]').val()
                                   // whatever: $('[name="whateverNameAttributeInYourForm"]').val()
                               };
                            }

                        },
                        regexp: {
                            regexp: /^.+$/,
                            message: ''
                        }
                    }
                },
                password: {
                    message: '密码无效',
                    validators: {
                        notEmpty: {
                            message: '密码不能为空'
                        },
                        stringLength: {
                            min: 6,
                            max: 30,
                            message: '密码长度必须在6到30之间'
                        },
                        identical: {//相同
                            field: 'password', //需要进行比较的input name值
                            message: '两次密码不一致'
                        },
                        different: {//不能和用户名相同
                            field: 'username',//需要进行比较的input name值
                            message: '不能和用户名相同'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_\.]+$/,
                            message: 'The username can only consist of alphabetical, number, dot and underscore'
                        }
                    }
                },
                repassword: {
                    message: '密码无效',
                    validators: {
                        notEmpty: {
                            message: '密码不能为空'
                        },
                        stringLength: {
                            min: 6,
                            max: 30,
                            message: '密码长度必须在6到30之间'
                        },
                        identical: {//相同
                            field: 'password',
                            message: '两次密码不一致'
                        },
                        different: {//不能和用户名相同
                            field: 'username',
                            message: '不能和用户名相同'
                        },
                        regexp: {//匹配规则
                            regexp: /^[a-zA-Z0-9_\.]+$/,
                            message: 'The username can only consist of alphabetical, number, dot and underscore'
                        }
                    }
                },
                email: {
                    validators: {
                        notEmpty: {
                            message: '邮件不能为空'
                        },
                        emailAddress: {
                            message: '请输入正确的邮件地址如：123@qq.com'
                        }
                    }
                },
                phone: {
                    message: 'The phone is not valid',
                    validators: {
                        notEmpty: {
                            message: '手机号码不能为空'
                        },
                        stringLength: {
                            min: 11,
                            max: 11,
                            message: '请输入11位手机号码'
                        },
                        regexp: {
                            regexp: /^1[3|5|8|9|6|7]{1}[0-9]{9}$/,
                            message: '请输入正确的手机号码'
                        }
                    }
                },
                stu_num: {
                    message: 'The student number is not valid',
                    validators: {
                        notEmpty: {
                            message: '学号不能为空'
                        },
                        stringLength: {
                            min: 11,
                            max: 11,
                            message: '请输入11位学号（不足11位首位用x填充）'
                        },
                        regexp: {
                            regexp: /^(x?[0-9]){10}|([0-9]{11})$/,
                            message: '请输入正确的学号'
                        }
                    }
                },
                invite: {
                    message: '邀请码',
                    validators: {
                        notEmpty: {
                            message: '邀请码不能为空'
                        },
                        stringLength: {
                            min: 8,
                            max: 8,
                            message: '请输入正确长度的邀请码'
                        },
                        regexp: {
                            regexp: /^[\w]{8}$/,
                            message: '请输入正确的邀请码(包含数字字母)'
                        }
                    }
                },
            }
        })

        //自动触发表单验证
        .on('success.form.bv', function (e) {//点击提交之后
            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data 提交至form标签中的action，result自定义
            $.post('/register_verify/', $form.serialize(), function (result) {
//do something...
                if(result == 'OK'){
                    window.location.href='/login/'
                }
            });
        });
});