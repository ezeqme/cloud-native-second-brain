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
themes: ["AI ML", "Security", "SRE Reliability"]
speakers: ["Raz Cohen", "Permit.io"]
sched_url: https://kccnceu2025.sched.com/event/1tx8a/redefining-access-control-scaling-policy-as-code-for-humans-and-ai-agents-raz-cohen-permitio
youtube_search_url: https://www.youtube.com/results?search_query=Redefining+Access+Control%3A+Scaling+Policy+as+Code+for+Humans+and+AI+Agents+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Redefining Access Control: Scaling Policy as Code for Humans and AI Agents - Raz Cohen, Permit.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Raz Cohen, Permit.io
- Schedule: https://kccnceu2025.sched.com/event/1tx8a/redefining-access-control-scaling-policy-as-code-for-humans-and-ai-agents-raz-cohen-permitio
- Busca YouTube: https://www.youtube.com/results?search_query=Redefining+Access+Control%3A+Scaling+Policy+as+Code+for+Humans+and+AI+Agents+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Redefining Access Control: Scaling Policy as Code for Humans and AI Agents.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8a/redefining-access-control-scaling-policy-as-code-for-humans-and-ai-agents-raz-cohen-permitio
- YouTube search: https://www.youtube.com/results?search_query=Redefining+Access+Control%3A+Scaling+Policy+as+Code+for+Humans+and+AI+Agents+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lQEYxCXVkVU
- YouTube title: Redefining Access Control: Scaling Policy as Code for Humans and AI Agents - Raz Cohen, Permit.io
- Match score: 0.96
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/redefining-access-control-scaling-policy-as-code-for-humans-and-ai-age/lQEYxCXVkVU.txt
- Transcript chars: 23194
- Keywords: access, control, understand, prompt, agents, response, actually, authorization, external, trying, important, advisory, policy, llm, pretty, action, asking, around

### Resumo baseado na transcript

And before I'm introducing myself, I actually wanted to talk a bit about what we are having today in London and maybe what we had last year in Paris. And actually last year I was speaking in CubeCon Paris and I remember walking in the booth aisles and uh most of the booths were around cost optimization and Kubernetes optimization and stuff like this maybe data optimization and when I walked today and yesterday I'm passionate traveler and food explorer and for the last eight or nine years I'm mostly uh digging into DevOps Kubernetes platform and this is I'm a bit nerdy about it and like most of you I guess that likes Kubernetes and today I'm solving access control and you might know this from kubernetes or other applications and role-based access control is just set up a role assign it to a user then you have access control for this user based on roles Right? So we need to in a way to guard rail this AI agent but we need to make sure we don't harm and we don't delay innovation and the challenges that we are talking about today when trying to control and get access control on need to make sure none of the data is getting exposed and leaked so in this case we need to filter the query we need to filter the table and you can see that also again we the prompt is getting filtered and we have

### Excerpt da transcript

Hey everyone, how are you today? Um, my name is Rasco and welcome everyone to CubeCon London. And before I'm introducing myself, I actually wanted to talk a bit about what we are having today in London and maybe what we had last year in Paris. And actually last year I was speaking in CubeCon Paris and I remember walking in the booth aisles and uh most of the booths were around cost optimization and Kubernetes optimization and stuff like this maybe data optimization and when I walked today and yesterday at CubeCon at the booths today um what I saw was a bit different because last year some products Some boosts were around optimization with chatbot of AI, right? Something like this. It was really cute, but it was like a question. Is it a real thing? Is it AI would be really answering all of our questions or is it just a buzzword or just a hype? And I think when I walk today in CubeCon, something else was was there. It was not just a chatbot. was not just a cute LLM that you write uh some words and it gives you some answers.

It's really different. You can see a lot of products fully AIdriven. You can talk to developers and de DevOps engineers and platform engineers that tell you that they not write code anymore, not writing YAML anymore. They only write prompts, right? It's completely different. And I know it's it can be a bit overwhelming to walk in any every pre presentation has this kind of cute images or every uh product try to show you yeah I'm we are doing the best with AI but uh I'm sorry to tell you this uh presentation is also going to talk about AI and most specifically about authorization and access control and how we can actually control the AI agents and not only just develop stuff without understanding what they are. And before diving into the actual uh topic of access control for AI agents, I wanted to talk about Isaac Asimov. And I'm almost sure that most of you know Isaac Asimov at least uh these books and his stories. So this guy was uh came from Russia to America in 1950 1940 and one of the books that he wrote was about robots.

Actually most of the books that he wrote was about science fiction and stuff like this but this one Iroot was about robots and in one of the stories in this book he was writing about the three laws of robotics. And the first law is makes sense, right? Do not harm the robot should not harm a human. The second is that the robot must obey a human. Then the third is that the robot should preserve themsel itself. So the
