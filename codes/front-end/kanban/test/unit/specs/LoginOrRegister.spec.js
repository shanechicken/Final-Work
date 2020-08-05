import Vue from 'vue'
import LoginOrRegister from '@/components/content/LoginOrRegister'

describe('LoginOrRegister.vue',()=>{
    it('载入时内容是否为空',()=>{
        let wrapper = mount(LoginOrRegister);
        expect(wrapper.vm.LoginData.project_id).toBe("");
        expect(wrapper.vm.LoginData.password).toBe("");
    })

    it('错误(空)用户名/密码不能登录',()=>{
        let wrapper = mount(LoginOrRegister);
        wrapper.find('button').trigger('click')
        expect(wrapper.vm.LoginData.project_id).toBe("");
        expect(wrapper.vm.LoginData.password).toBe("");
    })
})