from pathlib import Path

path = Path('10 - site-drflavio_metaia_v2.html')
text = path.read_text(encoding='utf-8')
old1 = '''                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-[#0a66c2] to-[#0957a5] flex items-center justify-center mb-5 shadow-lg shadow-[#0a66c2]/20">
                        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
                    </div>'''
new1 = '''                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-[#0a66c2] to-[#0957a5] flex items-center justify-center mb-5 shadow-lg shadow-[#0a66c2]/20">
                        <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                    </div>'''
old2 = '''                    <div class="w-14 h-14 rounded-2xl bg-slate-900 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364L12 7.636l-1.318-1.318a4.5 0 00-6.364 0z"/></svg>
                    </div>'''
new2 = '''                    <div class="w-14 h-14 rounded-2xl bg-slate-900 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>'''
old_check = '''                            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/></svg>
'''
new_check = '''                            <svg class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"/></svg>
'''
text = text.replace(old1, new1)
text = text.replace(old2, new2)
text = text.replace(old_check, new_check)
with open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(text)
print('updated')
