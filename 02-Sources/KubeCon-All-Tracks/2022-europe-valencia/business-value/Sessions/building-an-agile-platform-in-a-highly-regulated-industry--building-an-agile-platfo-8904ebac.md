---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Business Value"
themes: ["Platform Engineering"]
speakers: ["Fredrik Klingenberg", "Aurum AS", "Jonas Samuelson", "If Insurance"]
sched_url: https://kccnceu2022.sched.com/event/yttm/building-an-agile-platform-in-a-highly-regulated-industry-fredrik-klingenberg-aurum-as-jonas-samuelson-if-insurance
youtube_search_url: https://www.youtube.com/results?search_query=Building+an+Agile+Platform+in+a+Highly+Regulated+Industry+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Building an Agile Platform in a Highly Regulated Industry - Fredrik Klingenberg, Aurum AS & Jonas Samuelson, If Insurance

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Business Value]]
- Temas: [[Platform Engineering]]
- País/cidade: Spain / Valencia
- Speakers: Fredrik Klingenberg, Aurum AS, Jonas Samuelson, If Insurance
- Schedule: https://kccnceu2022.sched.com/event/yttm/building-an-agile-platform-in-a-highly-regulated-industry-fredrik-klingenberg-aurum-as-jonas-samuelson-if-insurance
- Busca YouTube: https://www.youtube.com/results?search_query=Building+an+Agile+Platform+in+a+Highly+Regulated+Industry+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Building an Agile Platform in a Highly Regulated Industry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttm/building-an-agile-platform-in-a-highly-regulated-industry-fredrik-klingenberg-aurum-as-jonas-samuelson-if-insurance
- YouTube search: https://www.youtube.com/results?search_query=Building+an+Agile+Platform+in+a+Highly+Regulated+Industry+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=urWojY1jxdc
- YouTube title: Building an Agile Platform in a Highly Regulated Industry - Fredrik Klingenberg & Jonas Samuelson
- Match score: 0.84
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/building-an-agile-platform-in-a-highly-regulated-industry/urWojY1jxdc.txt
- Transcript chars: 33751
- Keywords: platform, company, application, trying, question, insurance, obviously, already, applications, everything, having, scaling, course, technology, actually, working, linkedin, little

### Resumo baseado na transcript

hi and welcome to this presentation called building an azure platform in a highly regulated industry this is a joint project that you must robertson myself worked on for uh for almost a year but if the insurance company my name is freddie klimer as i mentioned i have this username for my time at uni you can find me on twitter obviously i'm on linkedin and slack as well i try to blog a little bit which out there i'm also a traffic and link the ambassador i try part of we already have it so let's do a small except of how we went about bootstrapping and building up everything and this ties into scaling as well we can then now scale the number of platform members working on all of the things we can now scale up the number of clusters and and rebuild it very quickly we kick things off with the very small batch script that i just wrote using azure cli we installed the secret controller this was the critical part where you need

### Excerpt da transcript

hi and welcome to this presentation called building an azure platform in a highly regulated industry this is a joint project that you must robertson myself worked on for uh for almost a year but if the insurance company my name is freddie klimer as i mentioned i have this username for my time at uni you can find me on twitter obviously i'm on linkedin and slack as well i try to blog a little bit which out there i'm also a traffic and link the ambassador i try to help out in those communities whenever i see people having somewhat of the similar problems that we have already been faced with yeah and my name is jonas samuelson i'm a platform lead at if insurance the main driver behind the platform we're going to present today i love tech teamwork and centralized agile platforms that provide value for dev teams and i'm an avid craft beer enthusiast maybe you can tell by looking at me so in today's talk we're trying to walk you through some of the considerations we had to make and hopefully a bit on how we solve them when creating this new agile platform service for dev teams in our company we have an agenda as well we'll kick things off with looking at if if insurance very brief introduction so to set the context a little bit there are constraints in the insurance company and that if of course and we'll look at those uh had a starting point there were some clusters already in place if the insurance company will look at what those starting points were and then we introduced some principles to help us to to guide us when building building a platform obviously we look into the actual building what tooling did we choose what kind of constraints were we under and what consideration did we do eunos will touch upon onboarding of the teams what were they what some of the challenges were moving to a more cloud native environment especially with the gear ops way of doing things and we'll have q a in the end yeah but first off a bit about if the insurance company so we're mainly operating in the nordic market we have a strong market position in the nordics with over 3.9 million customers and i saw the market and finance position today we're wholly owned subsidiary by the sampra group in finland since 2004 and we're they're listed on nasdaq in helsinki we have a solid basis in motor property insurance with sort of traditional lines of insurance products we give people the confidence today to shape our tomorrow that's our purpose but enough of some of the boring figures an
