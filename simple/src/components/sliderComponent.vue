<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 四张轮播图 -->
        <div v-show="nowIndex === index" class="slider-item" v-bind:class="['item'+[index+1]]" v-for="(item,index) in sliderImgList" v-bind:key="index">
            <a href="">
                <img v-bind:src="item.imgUrl" alt="">
            </a>
        </div>
        <h2 class="slider-title">{{sliderImgList[0].title}}</h2>
        <!-- 上一张下一张按钮 -->
        <a v-on:click="preHandler" class="btn pre-btn" href="javascript:void(0)">&lt;</a>
        <a v-on:click="nextHandler" class="btn next-btn" href="javascript:void(0)">&gt;</a>
        <!-- 下方圆点 -->
        <ul class="slider-dots">
            <li v-on:click="clickDots(index)" v-for="(item,index) in sliderImgList" v-bind:key="index">{{ index+1 }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList:[
                {
                    imgUrl:require('../assets/3.jpg'),
                    title:'第一章图'
                    },
                {
                    imgUrl:require('../assets/4.png'),
                     title:'第二章图'
                    },
                    {
                    imgUrl:require('../assets/5.jpg'),
                     title:'第三章图'
                    },
                    {
                    imgUrl:require('../assets/1.jpg'),
                     title:'第四章图'
                    },
            ]
        }
    },
    methods: {
        clickDots(index){
            this.nowIndex = index
        },
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex < 0){
                this.nowIndex = 3
            }
        },
        nextHandler(){
            this.autoPlay()
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex > 3){
                this.nowIndex = 0
            }
        },
        runInv(){
           this.invId = setInterval(this.autoPlay,2000)
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    created() {
        this.runInv()
    },
}
</script>

<style scoped>
    .slider-wrapper{
        width: 900px;
        height: 500px;
        background: red;
        position: relative;
    }
    .slider-item{
        width: 900px;
        height: 500px;
        text-align: center;
        line-height: 500px;
        font-size: 40px;
        position: absolute;
    }
    .item1{
        z-index: 100;
    }
    .item2{
        z-index: 90;
    }
    .item3{
        z-index: 80;
    }
    .item4{
        z-index: 70;
    }
    .slider-dots{
        position: absolute;
        right: 50px;
        bottom: 20px;
        z-index: 200;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background:#000000;
        color: #ffffff;
        text-align: center;
        line-height: 20px;
        float: left;
        margin: 0 10px;
        opacity: 0.6;
    }
    .btn{
        display: inline-block;
        width: 50px;
        height: 50px;
        color: #ffffff;
        background: #000000;
        font-size: 40px;
        text-align: center;
        line-height: 50px;
        position: absolute;
        top: 50%;
        margin-top: -25px;
        z-index: 300;
        opacity: 0.6;
    }
    .pre-btn{
        left: 10px;
    }
    .next-btn{
        right: 10px;
    }
    .slider-title{
        background: #000000;
        color: #ffffff;
        width: 100px;
        height: 30px;
        position: absolute;
        bottom: 10px;
        left: 10px;
        z-index: 400;
        font-size: 20px;
        text-align: center;
        line-height: 30px;
        opacity: 0.6;
    }
</style>