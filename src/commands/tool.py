from discord import (
    ApplicationContext as Context,
    ButtonStyle,
    Colour,
    Embed,
    EmbedField,
    EmbedFooter,
    SelectOption,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
    Select,
)

from lib.cog import CogExtension
from lib.functions import (
    get_now_time,
    wiki_search,
    calculator,
    translate,
    bullshit,
)

class SlashTool(CogExtension):
    pass
    @slash_command(description="翻譯功能")
    @option("語言", str, parameter_name="language", description="選擇要翻譯成的語言", choices=["繁中","簡中","英語","日語","印尼語"], required=False)
    @option("文字", str, parameter_name="text", description="文字", required=False)
    async def translate(self, ctx: Context, language: str = None, text: str = None):
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
                EmbedField("原文", f"```{text}```"),
                EmbedField(language, f"```{translate(text, translate_to[language])}```")
            ]
        ))

    @slash_command(description="字數轉換器")
    async def words(self, ctx: Context, text: str = None):
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
    @option("主題", str, parameter_name="topic", desciption="文章的主題", required=False)
    @option("字數", int, parameter_name="minlen", desciption="字數(上限1000)", required=False)
    async def bullshit(self, ctx: Context, topic: str = None, minlen: int = None):
        self.bot.log(ctx)
        if not topic or not minlen:
            return await ctx.respond(
                embed=Embed(
                    title="使用 /bullshit 唬爛產生器來生成文章!",
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
    @option("數學算式", str, parameter_name="formula", desciption="數學算式", required=False)
    async def math(self, ctx: Context, formula: str = None):
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
                description=f"```                                     ```",
                color=Colour.nitro_pink(),
            ),
            view=View(
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_1_{ctx.author.id}",
                    label="1",
                    row=1
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_2_{ctx.author.id}",
                    label="2",
                    row=1
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_3_{ctx.author.id}",
                    label="3",
                    row=1
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_4_{ctx.author.id}",
                    label="4",
                    row=2
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_5_{ctx.author.id}",
                    label="5",
                    row=2
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_6_{ctx.author.id}",
                    label="6",
                    row=2
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_7_{ctx.author.id}",
                    label="7",
                    row=3
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_8_{ctx.author.id}",
                    label="8",
                    row=3
                ),
                Button(
                    style= ButtonStyle.primary,
                    custom_id=f"math_9_{ctx.author.id}",
                    label="9",
                    row=3
                ),
                Button(
                    style=ButtonStyle.grey,
                    custom_id=f"math_(_{ctx.author.id}",
                    label="(",
                    row=4
                ),
                Button(
                    style=ButtonStyle.primary,
                    custom_id=f"math_0_{ctx.author.id}",
                    label="0",
                    row=4
                ),
                Button(
                    style=ButtonStyle.grey,
                    custom_id=f"math_)_{ctx.author.id}",
                    label=")",
                    row=4
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id=f"math_+_{ctx.author.id}",
                    label="+",
                    row=1
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id=f"math_-_{ctx.author.id}",
                    label="-",
                    row=2
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id=f"math_×_{ctx.author.id}",
                    label="×",
                    row=3
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id=f"math_÷_{ctx.author.id}",
                    label="÷",
                    row=4
                ),
                Button(
                    style=ButtonStyle.success,
                    custom_id=f"math_=_{ctx.author.id}",
                    label="=",
                    row=3
                ),
                Button(
                    style=ButtonStyle.danger,
                    custom_id=f"math_ac_{ctx.author.id}",
                    label="AC",
                    row=1
                ),
                Button(
                    style=ButtonStyle.danger,
                    custom_id=f"math_c_{ctx.author.id}",
                    label="C",
                    row=2
                ),
                Button(
                    style=ButtonStyle.gray,
                    custom_id=f"math_._{ctx.author.id}",
                    label=".",
                    row=4
                ),
            )
        )

    @slash_command(description="搜索維基百科")
    @option("關鍵字", str, parameter_name="keywords", description="搜索關鍵字", required=False)
    async def wiki(self, ctx: Context, keywords: str = None):
        self.bot.log(ctx)
        if not keywords:
            return await ctx.respond(
                embed=Embed(
                    title="使用 /wiki 來搜索維基百科!",
                    description="使用方法 /wiki `關鍵字`",
                    color=Colour.random(),
                    timestamp=get_now_time(),
                    footer=EmbedFooter("/wiki | Ganyu", self.bot.icon_url)
                )
            )
        
        results = wiki_search(tuple(keywords.split()))

        if not results: 
            return await ctx.respond(f"{self.bot.mention} 徹徹底底地搜索了一遍 但還是找不到結果..")
        
        await ctx.respond(
            embed=Embed(
                title=f"以下為有關\"{keywords}\"的搜索結果",
                color=Colour.random(),
                timestamp=get_now_time(),
                footer=EmbedFooter("/wiki | Ganyu", self.bot.icon_url)
            ), 
            view=View(
                Select(
                    placeholder="選擇相關的搜索結果",
                    options=[
                        SelectOption(**i) for i in [
                            {
                                "label": v[0],
                                "value": v[0],
                                "emoji": v[1]
                            } for v in zip(results, ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]) 
                        ]
                    ],
                    custom_id="wiki_select"
                ),
                timeout=None
            )
        )

def setup(bot):
    bot.add_cog(SlashTool(bot))