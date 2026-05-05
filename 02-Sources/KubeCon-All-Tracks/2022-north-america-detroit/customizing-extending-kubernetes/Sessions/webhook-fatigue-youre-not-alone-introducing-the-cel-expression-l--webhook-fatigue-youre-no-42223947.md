---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Joe Betz", "Google"]
sched_url: https://kccncna2022.sched.com/event/182Q6/webhook-fatigue-youre-not-alone-introducing-the-cel-expression-language-features-solving-this-problem-joe-betz-google
youtube_search_url: https://www.youtube.com/results?search_query=Webhook+Fatigue%3F+You%27re+Not+Alone%3A+Introducing+the+CEL+Expression+Language+Features+Solving+This+Problem+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Webhook Fatigue? You're Not Alone: Introducing the CEL Expression Language Features Solving This Problem - Joe Betz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Joe Betz, Google
- Schedule: https://kccncna2022.sched.com/event/182Q6/webhook-fatigue-youre-not-alone-introducing-the-cel-expression-language-features-solving-this-problem-joe-betz-google
- Busca YouTube: https://www.youtube.com/results?search_query=Webhook+Fatigue%3F+You%27re+Not+Alone%3A+Introducing+the+CEL+Expression+Language+Features+Solving+This+Problem+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Webhook Fatigue? You're Not Alone: Introducing the CEL Expression Language Features Solving This Problem.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Q6/webhook-fatigue-youre-not-alone-introducing-the-cel-expression-language-features-solving-this-problem-joe-betz-google
- YouTube search: https://www.youtube.com/results?search_query=Webhook+Fatigue%3F+You%27re+Not+Alone%3A+Introducing+the+CEL+Expression+Language+Features+Solving+This+Problem+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gJWMvsC7Mzo
- YouTube title: Webhook Fatigue? You're Not Alone: Introducing the CEL Expression Language Features...- Joe Betz
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/webhook-fatigue-youre-not-alone-introducing-the-cel-expression-languag/gJWMvsC7Mzo.txt
- Transcript chars: 33391
- Keywords: policy, validation, admission, pretty, cluster, write, support, language, control, probably, resources, expression, couple, trying, extension, actually, possible, author

### Resumo baseado na transcript

all right I'm going to go ahead and get started uh thank you everybody for coming this morning I'm excited about this talk I hope it is interesting to you all my name is Joe Betts I'm an engineer at Google I've been working on kubernetes for about five years I spent a couple years as an FCD maintainer and quite a bit of time as a contributor to Sig API Machinery where I've been working on extensibility features today we're going to talk about some enhancements that take advantage

### Excerpt da transcript

all right I'm going to go ahead and get started uh thank you everybody for coming this morning I'm excited about this talk I hope it is interesting to you all my name is Joe Betts I'm an engineer at Google I've been working on kubernetes for about five years I spent a couple years as an FCD maintainer and quite a bit of time as a contributor to Sig API Machinery where I've been working on extensibility features today we're going to talk about some enhancements that take advantage of something called the common expression language we're using this to try and address some of the problems that people have been facing with web hooks with kubernetes so I got quite a bit to cover today I'm going to get started by giving a brief history of web hooks that kind of motivate the problems that we're trying to solve then I'm going to dive in and give you a more detail explanation of what the common expression language is and why we think it is a useful enhancement it's going to help us solve problems I'll then dive into two major use cases the first use case is going to be crd validation which most people would prefer not to use a web hook to do and then the second one is admission control usually focusing on policy enforcement use cases I'll then wrap it up tie it together talk about the future and some areas where we can use some help so let's um get started by talking about the history of web admission web hooks so these were introduced back in kubernetes 1.7 roughly this is about five years ago when I was first starting to work on the project crds at the time were pretty young and there was a lot of people looking to use kubernetes for all sorts of things that it couldn't do natively and so the kind of the extension ecosystem was flourishing but not all the extension points were available at that time and I went back and looked at some of the documents explaining what people were trying to accomplish when they introduced admission web Hooks and I think they got the list pretty right because when you go and look at what books are used for today it more or less matches this list so they had identified that organizations needed better policy control that cloud providers needed better extension points to integrate with kubernetes and that extension authors need a better way to perform crd validation it's actually a pretty accurate list and at the time there was a couple different options there was a feature called initializers that was an alpha at the time there was th
