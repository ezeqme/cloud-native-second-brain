---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security"]
speakers: ["Anais Urlichs", "Rory McCune", "Aqua Security"]
sched_url: https://kccnceu2022.sched.com/event/ytsN/too-much-to-choose-making-sense-of-a-smorgasbord-of-security-standards-anais-urlichs-rory-mccune-aqua-security
youtube_search_url: https://www.youtube.com/results?search_query=Too+Much+to+Choose+%E2%80%93+Making+Sense+of+a+Smorgasbord+of+Security+Standards+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Too Much to Choose – Making Sense of a Smorgasbord of Security Standards - Anais Urlichs & Rory McCune, Aqua Security

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Spain / Valencia
- Speakers: Anais Urlichs, Rory McCune, Aqua Security
- Schedule: https://kccnceu2022.sched.com/event/ytsN/too-much-to-choose-making-sense-of-a-smorgasbord-of-security-standards-anais-urlichs-rory-mccune-aqua-security
- Busca YouTube: https://www.youtube.com/results?search_query=Too+Much+to+Choose+%E2%80%93+Making+Sense+of+a+Smorgasbord+of+Security+Standards+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Too Much to Choose – Making Sense of a Smorgasbord of Security Standards.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytsN/too-much-to-choose-making-sense-of-a-smorgasbord-of-security-standards-anais-urlichs-rory-mccune-aqua-security
- YouTube search: https://www.youtube.com/results?search_query=Too+Much+to+Choose+%E2%80%93+Making+Sense+of+a+Smorgasbord+of+Security+Standards+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yKqqCxvlDeE
- YouTube title: Too Much to Choose – Making Sense of a Smorgasbord of Security Standard- Anais Urlichs & Rory McCune
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/too-much-to-choose-making-sense-of-a-smorgasbord-of-security-standards/yKqqCxvlDeE.txt
- Transcript chars: 36259
- Keywords: security, cluster, standards, hardening, actually, running, secure, question, benchmark, compliance, reports, benchmarks, typically, standard, guidance, distribution, inside, source

### Resumo baseado na transcript

hi everyone and welcome along to this talk thanks very much for coming out this afternoon um to hear about security standards yep as ian said this is our talk is too much to choose making sense of a smorgasbord of security standards both of us pick the title before we realize that we have problems saying that word so we will try not to say smorgasbord too many times uh but we're okay so far so who are we um i am rumi kuhn i am a cloud native

### Excerpt da transcript

hi everyone and welcome along to this talk thanks very much for coming out this afternoon um to hear about security standards yep as ian said this is our talk is too much to choose making sense of a smorgasbord of security standards both of us pick the title before we realize that we have problems saying that word so we will try not to say smorgasbord too many times uh but we're okay so far so who are we um i am rumi kuhn i am a cloud native security advocate at aqua uh and i try to help out in various places in the community one of the reasons i'm doing this talk or is very excited to do this talk is one of the things i do is help maintain the cis benchmarks for docker and kubernetes which is something i've been doing for about five years now and that's kind of where i got a lot of ideas uh before this talk hi everybody my name is anna's orlais i'm the open source developer advocate at aqua security before that i was working a site reliability engineer i'm also a cncf ambassador and i run a youtube channel where i explore different technologies now i got started in the security space when i was joining aqua so all of this is still fairly new and that's also why i got really excited about giving this talk because it gave me the opportunity to dive into security standards so i hope to take you along and that you find out talk interesting cool so where do we start um you know i actually want to take one step back and say why do we start why do we actually care about security standards i i for me this comes from well i'm guessing that a lot of people here maybe even everyone here is running their workloads and their applications in kubernetes clusters and they're running production environments and once you've been running a production environment with kubernetes security with kubernetes for a while one of the questions someone is going to ask you is they're going to say is this secure you know you're running all your workloads if what you got secure and they might say well you're going to tell me it's secure but how am i going to prove it's secure you can you prove that this is secure and that's where security standards come in right because you can say well it's not just my opinion on what security things that need to be set here this is an authority who has said that this is the secure way to run this platform so that's i think why we're interested and why we want to think about what standards are how they work and which ones we might want to use so we're
