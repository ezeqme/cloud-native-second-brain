---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Runtime Containers"]
speakers: ["Angel M De Miguel Meana", "VMware", "Francisco Cabrera", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2nF/runwasi-webassembly-serverless-for-containerd-angel-m-de-miguel-meana-vmware-francisco-cabrera-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Runwasi%3A+WebAssembly+Serverless+for+Containerd+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Runwasi: WebAssembly Serverless for Containerd - Angel M De Miguel Meana, VMware & Francisco Cabrera, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Runtime Containers]]
- País/cidade: United States / Chicago
- Speakers: Angel M De Miguel Meana, VMware, Francisco Cabrera, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2nF/runwasi-webassembly-serverless-for-containerd-angel-m-de-miguel-meana-vmware-francisco-cabrera-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Runwasi%3A+WebAssembly+Serverless+for+Containerd+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Runwasi: WebAssembly Serverless for Containerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nF/runwasi-webassembly-serverless-for-containerd-angel-m-de-miguel-meana-vmware-francisco-cabrera-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Runwasi%3A+WebAssembly+Serverless+for+Containerd+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CbvMPGK8YyE
- YouTube title: Runwasi: WebAssembly Serverless for Containerd - Angel M De Miguel Meana & Francisco Cabrera
- Match score: 0.762
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/runwasi-webassembly-serverless-for-containerd/CbvMPGK8YyE.txt
- Transcript chars: 32420
- Keywords: actually, server, worker, application, assembly, specific, python, database, container, javascript, languages, better, running, containers, reactions, applications, having, already

### Resumo baseado na transcript

so good afternoon everyone thanks for being here uh my name is Francisco CA I'm a technical program manager at the AKs hybrid team at Microsoft and today with me is anel hello yeah so my name is anel I'm part of the VMware AI Labs team working on the on the exploration and developing web assembly related projects so yeah and today we'll be talking about how you can use run wasi in order to run web asem kind of a serverless approach uh specifically writing using contain and

### Excerpt da transcript

so good afternoon everyone thanks for being here uh my name is Francisco CA I'm a technical program manager at the AKs hybrid team at Microsoft and today with me is anel hello yeah so my name is anel I'm part of the VMware AI Labs team working on the on the exploration and developing web assembly related projects so yeah and today we'll be talking about how you can use run wasi in order to run web asem kind of a serverless approach uh specifically writing using contain and kubernetes um but before start I'll just I'll tell a little story so over the last two years I've been coming to you know different kind of kubernetes conferences we have assembly and every time I go back and I talk with you know my kubernetes team and I just talk about web assembly they always say hey feels great that's great but how I can use it how I can actually start using web assembly with kubernetes how I can actually bring it to customers and there is actually where I actually lack of good answers so when I was talking with anel talking about this talk we actually thought about okay how are we going to frame it so that we can help everyone actually start doing you know creating applications using web assembly specifically right with kubernetes um so let's go ahead and start it so we'll start talking a bit about you know web assembly then we're going to actually create a kubernetes sample app really simple um then anel will go over you know what is the was and worker servers how we actually do that migration process of moving from using Linux containers and start using web assembly modules um then we if we have time we'll go over how you you can actually extend this kind of a real simple app using serverless AI using web assembly using wnn and finally just you know some conclusions um so this that kind of like web is the next wave uh for those that are not familiar web assembly is this kind of a lowlevel assembly like kind of language with the this really compact uh binary format which has real kind of native performance um and has multiple benefits over containers and yeah sounds great but you know it's it's difficult right to actually start using web assembly um but if we go actually and see the cncf the annual survey in 2022 we see that container they said that containers are the new normal web assembly is the future again great but when you actually go and start seeing the numbers you see that 64% of these kind of respondents are using kubernetes in production environments uh
