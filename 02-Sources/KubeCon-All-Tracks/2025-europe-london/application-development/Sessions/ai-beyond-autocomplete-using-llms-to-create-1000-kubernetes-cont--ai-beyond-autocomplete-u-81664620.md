---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Justin Santa Barbara", "Walter Fender", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1txBL/ai-beyond-autocomplete-using-llms-to-create-1000-kubernetes-controllers-justin-santa-barbara-walter-fender-google
youtube_search_url: https://www.youtube.com/results?search_query=AI+Beyond+Autocomplete%3A+Using+LLMs+To+Create+1000+Kubernetes+Controllers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# AI Beyond Autocomplete: Using LLMs To Create 1000 Kubernetes Controllers - Justin Santa Barbara & Walter Fender, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Justin Santa Barbara, Walter Fender, Google
- Schedule: https://kccnceu2025.sched.com/event/1txBL/ai-beyond-autocomplete-using-llms-to-create-1000-kubernetes-controllers-justin-santa-barbara-walter-fender-google
- Busca YouTube: https://www.youtube.com/results?search_query=AI+Beyond+Autocomplete%3A+Using+LLMs+To+Create+1000+Kubernetes+Controllers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre AI Beyond Autocomplete: Using LLMs To Create 1000 Kubernetes Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txBL/ai-beyond-autocomplete-using-llms-to-create-1000-kubernetes-controllers-justin-santa-barbara-walter-fender-google
- YouTube search: https://www.youtube.com/results?search_query=AI+Beyond+Autocomplete%3A+Using+LLMs+To+Create+1000+Kubernetes+Controllers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_oIoaW5i-xE
- YouTube title: AI Beyond Autocomplete: Using LLMs To Create 1000 Kubernetes... Justin Santa Barbara & Walter Fender
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ai-beyond-autocomplete-using-llms-to-create-1000-kubernetes-controller/_oIoaW5i-xE.txt
- Transcript chars: 29281
- Keywords: llm, machine, simple, results, problems, better, write, actually, generate, resource, controllers, thousand, little, output, controller, complicated, solution, config

### Resumo baseado na transcript

And we are going to be talking to you today about um how we are using AI to generate uh those thousand controllers that make up Config Connector. Uh I'm both the software engineer and the EM on the config connector project as well as a few others. a customer will say, "Please fix this simple problem which I could fix in one line." And we're like, "Well, first we have to go ask the magic machine to do this and this and this." And it becomes a week-long uh escapade as it were. Um the problem with the Terraform or DCL magic machine was that that complexity, the complexity of the magic machine existed at runtime. We know that you know we will write better tooling to create particular problems we have and we we have people that are going to fix problems also um both you know ourselves on the config connector team and the community here right and we Um, but we also recognized that we didn't need the 100% reliability that we get with based tooling.

### Excerpt da transcript

Hello everybody. Good morning. Uh my name is Justin Santa Barbara. I am a software engineer at Google. I work on a number of open source projects related to Kubernetes. Uh one of which is Config Connector. And we are going to be talking to you today about um how we are using AI to generate uh those thousand controllers that make up Config Connector. This is Walter. Hello. I'm Walter Fender. Uh I also work on uh several open source Kubernetes projects. Uh I'm both the software engineer and the EM on the config connector project as well as a few others. Awesome. So we're not really going to dwell on config connector too much. This is really about the AI and Kubernetes controllers, but we are going to give a little bit of uh sort of our due diligence about you know how did we come to a place where we ended up having to write a thousand Kubernetes controllers. So the basic idea of config connector is we have rest GCP APIs to manage all the Google resources. Uh it's very simple similar to what you would do for many of the other cloud providers.

But those REST APIs are not inherently Kubernetes native. And so config connector is our attempt to write a KRM Kubernetes resource model that allows you to control all the Google APIs. And there are similar projects like ACK for AWS and ASO for Azure that have the same problem. And this means that if there are and there are a thousand different REST APIs to control various things, we need to have a thousand controllers uh each of which have their individual business logic that is going to to allow you to do this. So you know we have one CRD and controller for SQL instance. We have another one for IM service account. So then the question is well why not build on Terraform and we tried. Let me start with we tried. Uh and the problem we get is it ends up being a magic machine. You have one core place that is the guts of your controller and anytime you make changes to one resource to make something work some other resource breaks and that magic machine is really hard. And the more resources you try to do it this way, the more things break every time you make a change.

And it becomes just too complicated having this one very huge intricate magic machine that is the heart of your controller and and we want to emphasize that is not a knock on Terraform. This was true also of other things we tried as well. It is it is the nature of the magic machine that we become keepers of the magic machine. a customer will say, "Please fix
