import datetime

from discord import (
    ApplicationContext as Context,
    ButtonStyle,
    Colour,
    Embed,
    EmbedField,
    EmbedFooter,
    Member,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
)

from lib.cog import CogExtension

from lib.functions import (
    get_now_time,
    calculator,
    translate,
    bullshit,
)

class SlashTool(CogExtension):
    @slash_command(description="翻譯功能")
    @option("language", str, description="選擇要翻譯成的語言", choices=["繁中","簡中","英語","日語","印尼語"], required=False)
    async def translate(self, ctx: Context, language: str, * , text: str):
        self.bot.log(ctx)
        
        if not text:
            return await ctx.respond(embed=Embed(
                title="歡迎使用翻譯小工具!",
                description="此指令可以將各種語言翻譯成你想要的語言\n使用方法:/translate `要翻譯成的語言` `文字`",
                color=Colour.random(),
                timestamp=get_now_time()
            ))
            
        translate_to = {
            "繁中": "zh-TW",
            "簡中": "zh-CN",
            "英語": "en",
            "日語": "ja",
            "印尼語": "id"
        }
        
        await ctx.respond(embed=Embed(
            title="成功! 以下為翻譯結果",
            color=Colour.random(),
            timestamp=get_now_time(),
            thumbnail="https://th.bing.com/th/id/R.93d2c8f15964faae1e75331caf7d8fe0?rik=vl9rlcN9fh1oEw&pid=ImgRaw&r=0",
            footer=EmbedFooter("/translate", self.bot.icon_url),
            fields=[
                EmbedField("原文" f"```{text}```"),
                EmbedField(language, translate(text, translate_to[language]))
            ]
        ))

    @slash_command(description="字數轉換器")
    async def words(self, ctx: Context, *, text: str):
        if not text:
            return await ctx.respond(
                embed=Embed(
                    title="使用 /words 來轉換字數!",
                    description="使用方法: /words `句子`"
                )
            )
            
        await ctx.respond(
            embed=Embed(
                title="轉換成功!",
                description=f"此段句子一共有**{len(text)}**個字(含有**{len(list(filter(lambda x: x == ' ', text)))}**個空格)"
            )
        )

    @slash_command(description="唬爛產生器")
    @option("topic", str, desciption="主題", required=False)
    @option("minlen", int, desciption="字數(上限1000)", required=False)
    async def bullshit(self, ctx: Context, topic: str, minlen: int):
        if not topic or not minlen:
            return await ctx.respond(
                embed=Embed(
                title="使用 /bullshit唬爛產生器來生成文章!",
                description="使用方法 /bullshit `主題(如有空格需要用\"包起來)` `字數(上限1000)`",
                color=Colour.random(),
                timestamp=get_now_time(),
                footer=EmbedFooter("唬爛產生器", self.bot.icon_url)
            )
            )

        try:
            artcle = bullshit(topic, minlen)
            await ctx.respond(embed=Embed(
                title=topic,
                description=artcle
            ))

        except Exception as ex:
            self.bot.error(ctx, ex)
            return await ctx.respond("發生錯誤 請求未受到 API 回應", ephemeral=True)

    @slash_command(description="計算機")
    @option("formula", str, desciption="算式", required=False)
    async def math(self, ctx: Context, formula: str):
        self.bot.log(ctx)
        if formula:
            return await ctx.respond(embed=Embed(
                title="計算機",
                description="結果如下",
                color=Colour.random(),
                timestamp=get_now_time(),
                footer=EmbedFooter("/math | Ganyu", self.bot.icon_url),
                fields=[
                    EmbedField("原始算式", f"```{formula}```"),
                    EmbedField("計算結果", f"```{calculator(formula)}```")
                ]
            ))

        await ctx.respond(
            embed=Embed(
                title="計算機",
                description=f"```                                        ```",
                color=Colour.random(),
                timestamp=get_now_time(),
                footer=EmbedFooter("/math | Ganyu", self.bot.icon_url),
            ),
            view=View(
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_1",
                    label="1",
                    row=1
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_2",
                    label="2",
                    row=1
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_3",
                    label="3",
                    row=1
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_4",
                    label="4",
                    row=2
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_5",
                    label="5",
                    row=2
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_6",
                    label="6",
                    row=2
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_7",
                    label="7",
                    row=3
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_8",
                    label="8",
                    row=3
                ),
                Button(
                    style= ButtonStyle.primary,
                    custom_id="math_9",
                    label="9",
                    row=3
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id="math_0",
                    label="0",
                    row=4
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id="math_.",
                    label=".",
                    row=4
                ),
                Button(
                    style=ButtonStyle.success,
                    custom_id="math_=",
                    label="=",
                    row=3
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id="math_+",
                    label="+",
                    row=1
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id="math_-",
                    label="-",
                    row=2
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id="math_×",
                    label="×",
                    row=3
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id="math_÷",
                    label="÷",
                    row=4
                ),
                Button(
                    style=ButtonStyle.danger,
                    custom_id="math_ac",
                    label="AC",
                    row=1
                ),
                Button(
                    style=ButtonStyle.danger,
                    custom_id="math_c",
                    label="C",
                    row=2
                ),
                Button(
                    style=ButtonStyle.grey,
                    custom_id="math_(",
                    label="(",
                    row=4
                ),
                Button(
                    style=ButtonStyle.grey,
                    custom_id="math_)",
                    label=")",
                    row=4
                )
            )
        )


    @discord.application_command(description="搜索維基百科")
    async def wiki(self,ctx,keywords:discord.Option(str,"搜索關鍵字")):
        await tool.wikiInfo(ctx,keywords,self.bot)

def setup(bot):
    bot.add_cog(SlashTool(bot))