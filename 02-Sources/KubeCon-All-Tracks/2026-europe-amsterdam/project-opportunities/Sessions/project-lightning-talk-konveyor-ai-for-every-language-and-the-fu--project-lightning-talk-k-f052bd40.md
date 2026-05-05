---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Shaaf Syed", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EIxA/project-lightning-talk-konveyor-ai-for-every-language-and-the-future-of-app-modernization-shaaf-syed-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Konveyor+AI+for+Every+Language+and+the+Future+of+App+Modernization+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Konveyor AI for Every Language and the Future of App Modernization - Shaaf Syed, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shaaf Syed, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EIxA/project-lightning-talk-konveyor-ai-for-every-language-and-the-future-of-app-modernization-shaaf-syed-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Konveyor+AI+for+Every+Language+and+the+Future+of+App+Modernization+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Konveyor AI for Every Language and the Future of App Modernization.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EIxA/project-lightning-talk-konveyor-ai-for-every-language-and-the-future-of-app-modernization-shaaf-syed-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Konveyor+AI+for+Every+Language+and+the+Future+of+App+Modernization+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6FNR4jGox9w
- YouTube title: Project Lightning Talk: Konveyor AI for Every Language and the Future of App Moderniza... Shaaf Syed
- Match score: 0.999
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-konveyor-ai-for-every-language-and-the-future-o/6FNR4jGox9w.txt
- Transcript chars: 5810
- Keywords: analysis, language, static, results, agents, application, conveyor, understand, context, memory, modernization, protocol, enterprise, engine, golang, change, server, months

### Resumo baseado na transcript

Your boss comes in one day says hey I would like to run this on Kubernetes. stubs, serialization, pets, taking care, no clustering can fail, etc., etc., lots of troubles. the other things in the code we want to fix them as well so that's where agents come in they do compilation they do from validation testing etc and sanitize those results and start working with all the other problems and keep on fixing issues

### Excerpt da transcript

So my name is Sha. I'll speak about application modernization coming up the stack a bit. Um if you've seen this code uh don't raise your hand. Kind of tells me how uh we have the same age. You could say like that right? So this is about 30 years old enterprise Java bean. Your boss comes in one day says hey I would like to run this on Kubernetes. What do you do? Uh you look at the protocol and this is what you see. Um fun stuff. stubs, serialization, pets, taking care, no clustering can fail, etc., etc., lots of troubles. So, how do we how do we solve that? So, in the conveyor community, which is trying to solve the application modernization problem for almost every other language uh we have a set of uh solutions for it. And one of the main core things that we do is uh an analysis engine. We analyze the source static code analysis. Uh we try to understand things like Java, things like Golang etc. Uh we try to make sure that there are some guidelines for for people like me who don't program that much that okay if you want to change a component that uses IOP or uh messaging or transactions etc.

what could be the different things you could do in order for it to run on a platform like Kubernetes. So we um we do the static code analysis engine which is uh part of the conveyor community. Um and then we connect it with the language server protocol. The language server protocol being uh something that gives us this nice view of uh what the code is doing, what the code paths are etc etc. Um and uh gives us that implementation analysis rules. uh we can we can have multiple rules for it. What we've done recently in last six months is that we've added the support for C um Golang, Python and NodeJS which means that now if you were going to take an application run a static code analysis on it, it's going to report to you, you know, hey, maybe you should use some secrets and config maps by the way, right? stuff like that that's going to give you ideas around uh and be able to generate code since everybody talks about AI. Uh we can now use that static code analysis, throw that using some context engineering into the large language model and get some good results.

Before I do that, here's a report which kind of gives another Java application. Since I love Java so much, I thought I should give you a preview of that. uh it shows you about um a simple uh you know line that basically is offensive. Offensive in the sense that it won't run on Kubernetes. It needs some context.
