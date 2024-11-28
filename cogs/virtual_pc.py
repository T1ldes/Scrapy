import discord
from discord.ext import commands
import asyncio
import base64
from io import BytesIO
from playwright.async_api import async_playwright

class TicTacToeControls(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="⬆️ Move Up", row=0, style=discord.ButtonStyle.primary)
    async def move_up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="mouse_move", coordinate=[0, -50])
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬇️ Move Down", row=0, style=discord.ButtonStyle.primary)
    async def move_down(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="mouse_move", coordinate=[0, 50])
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬅️ Move Left", row=1, style=discord.ButtonStyle.primary)
    async def move_left(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="mouse_move", coordinate=[-50, 0])
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="➡️ Move Right", row=1, style=discord.ButtonStyle.primary)
    async def move_right(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="mouse_move", coordinate=[50, 0])
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="🖱️ Click", row=2, style=discord.ButtonStyle.success)
    async def click(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="left_click")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬅️ Back", row=3, style=discord.ButtonStyle.secondary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Games Menu", color=discord.Color.blue()),
            view=GamesView(self.cog)
        )


class Game2048Controls(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="⬆️", row=0, style=discord.ButtonStyle.primary)
    async def up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="key", text="ArrowUp")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬇️", row=2, style=discord.ButtonStyle.primary)
    async def down(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="key", text="ArrowDown")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬅️", row=1, style=discord.ButtonStyle.primary)
    async def left(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="key", text="ArrowLeft")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="➡️", row=1, style=discord.ButtonStyle.primary)
    async def right(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="key", text="ArrowRight")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬅️ Back", row=3, style=discord.ButtonStyle.secondary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Games Menu", color=discord.Color.blue()),
            view=GamesView(self.cog)
        )

class SnakeControls(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="⬆️", row=0, style=discord.ButtonStyle.primary)
    async def up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "ArrowUp")

    @discord.ui.button(label="⬇️", row=2, style=discord.ButtonStyle.primary)
    async def down(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "ArrowDown")

    @discord.ui.button(label="⬅️", row=1, style=discord.ButtonStyle.primary)
    async def left(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "ArrowLeft")

    @discord.ui.button(label="➡️", row=1, style=discord.ButtonStyle.primary)
    async def right(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "ArrowRight")

    @discord.ui.button(label="⬅️ Back", row=3, style=discord.ButtonStyle.secondary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Games Menu", color=discord.Color.blue()),
            view=GamesView(self.cog)
        )



class MainView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="🎮 Games", row=0, style=discord.ButtonStyle.primary)
    async def games(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Games Menu", color=discord.Color.blue()),
            view=GamesView(self.cog)
        )

    @discord.ui.button(label="🌐 Browser", row=0, style=discord.ButtonStyle.primary)
    async def browser(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(BrowserModal(self.cog))

    @discord.ui.button(label="💻 System", row=0, style=discord.ButtonStyle.primary)
    async def system(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="System Controls", color=discord.Color.blue()),
            view=SystemControls(self.cog)
        )

class GamesView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog
        self.games = {
            "Tic Tac Toe": "https://playtictactoe.org",
            "2048": "https://play2048.co",
            "Snake": "https://playsnake.org"
        }
        self._add_game_buttons()

    def _add_game_buttons(self):
        for idx, (name, url) in enumerate(self.games.items()):
            button = discord.ui.Button(
                label=name,
                custom_id=f"game_{idx}",
                row=idx//2,
                style=discord.ButtonStyle.primary
            )
            button.callback = self.make_callback(url)
            self.add_item(button)

        back_button = discord.ui.Button(
            label="⬅️ Back",
            row=2,
            style=discord.ButtonStyle.secondary
        )
        back_button.callback = self.back_to_main
        self.add_item(back_button)

    def make_callback(self, url):
        async def callback(interaction: discord.Interaction):
            await interaction.response.defer()
            await self.cog.launch_game(interaction, url)
        return callback

    async def back_to_main(self, interaction: discord.Interaction):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Main Menu", color=discord.Color.blue()),
            view=MainView(self.cog)
        )
class SystemControls(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="📝 Terminal", row=0, style=discord.ButtonStyle.green)
    async def terminal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(TerminalModal(self.cog))

    @discord.ui.button(label="📂 Files", row=0, style=discord.ButtonStyle.primary)
    async def files(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.open_file_manager(interaction)

    @discord.ui.button(label="📊 System Info", row=0, style=discord.ButtonStyle.primary)
    async def system_info(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.show_system_info(interaction)

    @discord.ui.button(label="⬅️ Back", row=1, style=discord.ButtonStyle.gray)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Main Menu", color=discord.Color.blue()),
            view=MainView(self.cog)
        )

class TerminalModal(discord.ui.Modal):
    def __init__(self, cog):
        super().__init__(title="Terminal Command")
        self.cog = cog
        self.command = discord.ui.TextInput(
            label="Enter command",
            placeholder="e.g., ls -la",
            style=discord.TextStyle.paragraph,
            required=True
        )
        self.add_item(self.command)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            # Execute command directly without any arguments
            print(self.command)
            result = self.cog.instance.bash(str(self.command.value))
            print(result)
            embed = discord.Embed(
                title="Terminal Output",
                description=f"```bash\n{result}\n```",
                color=discord.Color.green()
            )
            await interaction.followup.send(embed=embed)
        except Exception as e:
            print(f"Terminal error: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

class BrowserModal(discord.ui.Modal):
    def __init__(self, cog):
        super().__init__(title="Enter URL")
        self.cog = cog
        self.url = discord.ui.TextInput(
            label="URL",
            placeholder="https://example.com",
            required=True
        )
        self.add_item(self.url)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            await self.cog.page.goto(self.url.value, wait_until="networkidle")
            screenshot = await asyncio.to_thread(self.cog.instance.screenshot)
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
            embed = discord.Embed(title=f"Browsing: {self.url.value}", color=discord.Color.green())
            embed.set_image(url="attachment://screen.png")
            await interaction.followup.send(embed=embed, file=file, view=BrowserControls(self.cog))
        except Exception as e:
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

class BrowserControls(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="⬆️ Scroll Up", row=0, style=discord.ButtonStyle.primary)
    async def scroll_up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.page.evaluate("window.scrollBy(0, -300)")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬇️ Scroll Down", row=0, style=discord.ButtonStyle.primary)
    async def scroll_down(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.page.evaluate("window.scrollBy(0, 300)")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="🖱️ Click", row=0, style=discord.ButtonStyle.success)
    async def click(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.cog.instance.computer(action="left_click")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="🔄 Refresh", row=1, style=discord.ButtonStyle.primary)
    async def refresh(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await self.cog.page.reload(wait_until="networkidle")
        screenshot = self.cog.instance.screenshot()
        file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            attachments=[file]
        )

    @discord.ui.button(label="⬅️ Back", row=1, style=discord.ButtonStyle.secondary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if self.cog.screenshot_task:
            self.cog.screenshot_task.cancel()
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            embed=discord.Embed(title="Main Menu", color=discord.Color.blue()),
            view=MainView(self.cog)
        )
class GameControls(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="1", row=0, style=discord.ButtonStyle.primary)
    async def btn_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "1")

    @discord.ui.button(label="2", row=0, style=discord.ButtonStyle.primary)
    async def btn_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "2")

    @discord.ui.button(label="3", row=0, style=discord.ButtonStyle.primary)
    async def btn_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "3")

    @discord.ui.button(label="4", row=1, style=discord.ButtonStyle.primary)
    async def btn_4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "4")

    @discord.ui.button(label="5", row=1, style=discord.ButtonStyle.primary)
    async def btn_5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "5")

    @discord.ui.button(label="6", row=1, style=discord.ButtonStyle.primary)
    async def btn_6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "6")

    @discord.ui.button(label="7", row=2, style=discord.ButtonStyle.primary)
    async def btn_7(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "7")

    @discord.ui.button(label="8", row=2, style=discord.ButtonStyle.primary)
    async def btn_8(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "8")

    @discord.ui.button(label="9", row=2, style=discord.ButtonStyle.primary)
    async def btn_9(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.send_key(interaction, "9")

    @discord.ui.button(label="⬅️ Back to Games", row=3, style=discord.ButtonStyle.secondary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            embed=discord.Embed(title="Games Menu", color=discord.Color.blue()),
            view=GamesView(self.cog)
        )

class VirtualPC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.instance = None
        self.playwright = None
        self.browser = None
        self.page = None
        self.loading_gif = "https://i.gifer.com/ZKZx.gif"
        self.screenshot_task = None

    @commands.command()
    async def start(self, ctx):
        loading_embed = discord.Embed(
            title="🖥️ Starting Virtual PC...",
            description="```\n⚙️ Initializing system...\n```",
            color=discord.Color.blue()
        )
        loading_embed.set_image(url=self.loading_gif)
        message = await ctx.send(embed=loading_embed)

        try:
            print("Starting Scrapybara instance...")
            self.instance = self.bot.scrapybara.start(
                instance_type="medium",
                region="us-west-1"
            )
            print("Instance started successfully")

            print("Starting browser session...")
            cdp_url = self.instance.browser.start()
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.connect_over_cdp(cdp_url)
            self.page = await self.browser.new_page()
            print("Browser session started successfully")

            print("Starting screenshot loop...")
            self.screenshot_task = asyncio.create_task(self.start_screenshot_loop(message))

            success_embed = discord.Embed(
                title="🖥️ Virtual PC Ready",
                description="```\n✅ System initialized successfully!\n```",
                color=discord.Color.green()
            )
            screenshot = self.instance.screenshot()
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
            success_embed.set_image(url="attachment://screen.png")
            
            await message.edit(
                embed=success_embed,
                attachments=[file],
                view=MainView(self)
            )
            print("Startup complete!")

        except Exception as e:
            print(f"Error during startup: {str(e)}")
            error_embed = discord.Embed(
                title="❌ Error",
                description=f"```\n{str(e)}\n```",
                color=discord.Color.red()
            )
            await message.edit(embed=error_embed)

    async def start_screenshot_loop(self, message):
        print("Starting screenshot update loop...")
        while True:
            try:
                if self.page and hasattr(self, 'is_browsing') and self.is_browsing:
                    screenshot = self.instance.screenshot()
                    embed = message.embeds[0]
                    file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
                    embed.set_image(url="attachment://screen.png")
                    await message.edit(embed=embed, attachments=[file])
                await asyncio.sleep(5)
            except Exception as e:
                print(f"Screenshot loop error: {str(e)}")
                break

    async def execute_bash(self, command: str) -> str:
        try:
            # Execute command directly without any slicing
            result = self.instance.bash(command)
            return result if result else "Command executed successfully."
        except Exception as e:
            print(f"Terminal error: {str(e)}")
            return f"Error: {str(e)}"

    async def open_file_manager(self, interaction: discord.Interaction):
        try:
            self.instance.bash("DISPLAY=:1 xdg-open .")
            screenshot = self.instance.screenshot()
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
            embed = discord.Embed(title="File Manager", color=discord.Color.green())
            embed.set_image(url="attachment://screen.png")
            await interaction.followup.send(embed=embed, file=file)
        except Exception as e:
            print(f"File manager error: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

    async def show_system_info(self, interaction: discord.Interaction):
        try:
            commands = [
                "uname -a",
                "free -h",
                "df -h",
                "cat /proc/cpuinfo | grep 'model name' | head -1",
                "uptime"
            ]
            results = []
            for cmd in commands:
                result = self.instance.bash(cmd)
                results.append(f"$ {cmd}\n{result}\n")
            
            embed = discord.Embed(
                title="System Information",
                description=f"```bash\n{''.join(results)}```",
                color=discord.Color.green()
            )
            await interaction.followup.send(embed=embed)
        except Exception as e:
            print(f"System info error: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

    async def launch_game(self, interaction: discord.Interaction, url: str):
        try:
            
            game_type = url.split("//")[1].split(".")[0]
            
            loading_embed = discord.Embed(title="Loading Game...", color=discord.Color.blue())
            loading_embed.set_image(url=self.loading_gif)
            await interaction.followup.send(embed=loading_embed)
            
            await self.page.goto(url, wait_until="load", timeout=30000)
            screenshot = self.instance.screenshot()
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "game.png")
            
            game_embed = discord.Embed(title=f"Playing {game_type.title()}", color=discord.Color.green())
            game_embed.set_image(url="attachment://game.png")
            
            # Create appropriate view based on game type
            if "tictactoe" in url:
                view = TicTacToeControls(self)
            elif "2048" in url:
                view = Game2048Controls(self)
            else:
                view = GameControls(self)
                
            # Use followup.edit_message instead of edit_original_response
            await interaction.followup.edit_message(
                message_id=interaction.message.id,
                embed=game_embed,
                attachments=[file],
                view=view
            )
        except Exception as e:
            print(f"Error launching game: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

    async def move_mouse(self, interaction: discord.Interaction, coordinates: list):
        try:
            self.instance.computer(action="mouse_move", coordinate=coordinates)
            screenshot = self.instance.screenshot()
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
            await interaction.followup.edit_message(
                message_id=interaction.message.id,
                attachments=[file]
            )
        except Exception as e:
            print(f"Error moving mouse: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

    async def mouse_click(self, interaction: discord.Interaction):
        try:
            self.instance.computer(action="left_click")
            screenshot = self.instance.screenshot()
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
            await interaction.followup.edit_message(
                message_id=interaction.message.id,
                attachments=[file]
            )
        except Exception as e:
            print(f"Error clicking: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

    async def send_key(self, interaction: discord.Interaction, key: str):
        try:
            self.instance.computer(action="key", text=key)
            screenshot = self.instance.screenshot()
            file = discord.File(BytesIO(base64.b64decode(screenshot)), "screen.png")
            await interaction.followup.edit_message(
                message_id=interaction.message.id,
                attachments=[file]
            )
        except Exception as e:
            print(f"Error sending key: {str(e)}")
            await interaction.followup.send(f"Error: {str(e)}", ephemeral=True)

    async def end_session(self, interaction: discord.Interaction):
        try:
            print("Ending session...")
            if self.screenshot_task:
                self.screenshot_task.cancel()
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
            if self.instance:
                self.instance.browser.stop()
                self.instance.stop()
            
            embed = discord.Embed(
                title="Session Ended",
                description="Virtual PC has been shut down",
                color=discord.Color.red()
            )
            await interaction.response.edit_message(embed=embed, view=None)
            print("Session ended successfully")
        except Exception as e:
            print(f"Error ending session: {str(e)}")
            await interaction.response.send_message(f"Error: {str(e)}", ephemeral=True)

    
async def setup(bot):
    await bot.add_cog(VirtualPC(bot))
