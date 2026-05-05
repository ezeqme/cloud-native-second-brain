---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Stefan Schimanski", "Upbound", "Mangirdas Judeikis", "Cast AI", "Sebastian Scheele", "Kubermatic"]
sched_url: https://kccnceu2024.sched.com/event/1YePC/why-kubernetes-is-inappropriate-for-platforms-and-how-to-make-it-better-stefan-schimanski-upbound-mangirdas-judeikis-cast-ai-sebastian-scheele-kubermatic
youtube_search_url: https://www.youtube.com/results?search_query=Why+Kubernetes+Is+Inappropriate+for+Platforms%2C+and+How+to+Make+It+Better.+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Why Kubernetes Is Inappropriate for Platforms, and How to Make It Better. - Stefan Schimanski, Upbound; Mangirdas Judeikis, Cast AI; Sebastian Scheele, Kubermatic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Stefan Schimanski, Upbound, Mangirdas Judeikis, Cast AI, Sebastian Scheele, Kubermatic
- Schedule: https://kccnceu2024.sched.com/event/1YePC/why-kubernetes-is-inappropriate-for-platforms-and-how-to-make-it-better-stefan-schimanski-upbound-mangirdas-judeikis-cast-ai-sebastian-scheele-kubermatic
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Kubernetes+Is+Inappropriate+for+Platforms%2C+and+How+to+Make+It+Better.+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Why Kubernetes Is Inappropriate for Platforms, and How to Make It Better..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePC/why-kubernetes-is-inappropriate-for-platforms-and-how-to-make-it-better-stefan-schimanski-upbound-mangirdas-judeikis-cast-ai-sebastian-scheele-kubermatic
- YouTube search: https://www.youtube.com/results?search_query=Why+Kubernetes+Is+Inappropriate+for+Platforms%2C+and+How+to+Make+It+Better.+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7op_r9R0fCo
- YouTube title: Why Kubernetes Is Inappropriate for Platforms, and How to Make It Better
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/why-kubernetes-is-inappropriate-for-platforms-and-how-to-make-it-bette/7op_r9R0fCo.txt
- Transcript chars: 31125
- Keywords: platform, cluster, basically, clusters, platforms, course, personas, region, compute, create, everything, similar, controller, tooling, application, workspace, deploy, consume

### Resumo baseado na transcript

who's here for the Lego talk in the audience now hence there will be plenty of Lego and there's a coincidence there's a Lego talk in the Next Room so but we not from Lego but we like Lego so it's everywhere in the talk all right so before we start a short introduction who is who here on stage so hey I'm MJ M I work at cast we do cost optimization and I'm interested in control planes this is why I'm here Sebastian one of the founders of

### Excerpt da transcript

who's here for the Lego talk in the audience now hence there will be plenty of Lego and there's a coincidence there's a Lego talk in the Next Room so but we not from Lego but we like Lego so it's everywhere in the talk all right so before we start a short introduction who is who here on stage so hey I'm MJ M I work at cast we do cost optimization and I'm interested in control planes this is why I'm here Sebastian one of the founders of kmetic and yeah all we do is all around control planes yeah more less the same for me Stefan I'm at upbound doing control plans you know myself probably from CS I was very involved there so if you use them that's probably partly my co my code so our talk today is why kubernetes is inappropriate for platform so this is of course a big claim and how to make it better so this talk is about ideas it's not about setting a project or a product or anything like that so it's more more about um not just accepting Cube but thinking about how we would have to change Cube to get something better for platforms that's our motivation today and we were thinking okay the last days were all about Ai and ml so let's build an AI and ml platform here um and keep in mind we like Cube but we also want to show you what potentially could be improved or what we dislike so let's start with this experiment so if you want to build a platform uh the first thing what we need is we need to provide our developers some kind of possibilities to create objects so we need some kind of objects we have S in kubernetes we have CS we can create like an object uh called model and different teams can create it different user can create it so it's there perfect the next thing as we want to provide our platform to different teams we need to have some separation we have this also in kubernetes called namespaces so we can give each team its own name space they can deploy this object and it's completely separated we can also separate it by our so also this we have in kubernetes and of course what we want to have is a uniformed API so potentially we need even more objects and it should every time follow similar principles and kubernetes gives this uh to us and if in the future we want to add another AI service or we want to add a database service it should not be a complete different way how to consume this how to operate with this service so this part we have perfect let's go further the next step is we now have this objects what to do with it and kubernetes we have this
