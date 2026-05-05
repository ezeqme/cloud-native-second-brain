---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Matthew Bates", "Cofide"]
sched_url: https://kccnceu2025.sched.com/event/1tx8O/iam-agent-identity-for-autonomous-ai-matthew-bates-cofide
youtube_search_url: https://www.youtube.com/results?search_query=IAM%2C+Agent%3A+Identity+for+Autonomous+AI+CNCF+KubeCon+2025
slides: []
status: parsed
---

# IAM, Agent: Identity for Autonomous AI - Matthew Bates, Cofide

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Matthew Bates, Cofide
- Schedule: https://kccnceu2025.sched.com/event/1tx8O/iam-agent-identity-for-autonomous-ai-matthew-bates-cofide
- Busca YouTube: https://www.youtube.com/results?search_query=IAM%2C+Agent%3A+Identity+for+Autonomous+AI+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre IAM, Agent: Identity for Autonomous AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8O/iam-agent-identity-for-autonomous-ai-matthew-bates-cofide
- YouTube search: https://www.youtube.com/results?search_query=IAM%2C+Agent%3A+Identity+for+Autonomous+AI+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CvGbwn5ZrFg
- YouTube title: IAM, Agent: Identity for Autonomous AI - Matthew Bates, Cofide
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/iam-agent-identity-for-autonomous-ai/CvGbwn5ZrFg.txt
- Transcript chars: 36651
- Keywords: actually, access, identity, pretty, request, perhaps, effectively, tokens, workload, interesting, probably, wanted, already, spiffy, llm, context, course, number

### Resumo baseado na transcript

It's really close to our hearts and all of the open standards and tools in the CNCF are ones that we use. Um I don't know if anyone can remember back to the last time this was in London, uh 2016. I sort of thought like if I was to do this and I was something quite canonical um so to keep things simple for the purposes demonstration, but if I was to build like a chat agent, a customer service assistant, you know, we're all But what I realized is that when building this uh and sort of putting my sort of security hat on, I realized that I was storing up a huge amount of risk when building this prototype. Um and hopefully I'm sure some of you may have already come across these as you've been building agents when you know you've been putting into production the security teams have been asking you have you thought about authentication have you thought about authorization um Uh, and we've got the challenge of identifying the user as well that have made this original request, right?

### Excerpt da transcript

Okay, good morning everyone. Welcome. I think we're gonna make a start. Thanks so much for coming. Uh my name is uh Matt Bates. I'm a founder at a company called Kofi, a UK startup. We focus on workload identity. It's really close to our hearts and all of the open standards and tools in the CNCF are ones that we use. Um so pleasure to be back in London. Um I don't know if anyone can remember back to the last time this was in London, uh 2016. Just a quick show of hands. Is anyone here at the Yeah, I thought Ben was. Yeah. Um, but yeah, the room I think the keynote room was uh smaller than this. Uh, much smaller than this, in fact. So, great to see how far we've come. So, today I'm going to be talking about something I'm sure you've probably not heard much about at the moment, which is AI. Um, no, specifically, we're going to be talking about um IM uh for AI agents and some of the interesting challenges um that it that it presents. So, hopefully this will give you some food for thought. you can see some existing tools, techniques that you can use today in the CNCF.

Um, and I'm also going to sort of shed some light I guess on some of those challenges and some of the ongoing efforts within the CNCF um and beyond um for solving some of these challenges. It's hopefully um super useful for you today and to take away with you. Um so we I guess we we've all heard about AI. We all use it. Um quick show of hands. In fact, is everybody using AI here? Is everybody using generative? Yeah. Okay. I probably don't need to ask. Um, so we're all very used to using like generative AI, generally speaking. Um, yeah, a lot of us now using it for coding. I do probably more vibe coding than I probably should be doing. Um, but we're all finding it incredibly useful in our daily lives. And I think by the day, by, you know, by the week, things are changing. Really, what I wanted to focus on specifically are our agents. Um, and yes, this is some generative AI from OpenAI. Um, you might notice a few of those throughout the talk. Um, but an a AI agent is one that has is one that's more autonomous, right?

We give it a task and rather than just relying on sort of some of the generative AI we've been used to where we engage in a conversation, it responds to us um using an LLM uh gives us some kind of text or some kind of other media. Um, the agent can actually have some decision- making and some reasoning capability. So it can actually understand the task that we're asking it um and can
