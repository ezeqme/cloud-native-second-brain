---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Lucas Käldström"]
sched_url: https://kccnceu2022.sched.com/event/ytr4/understanding-kubernetes-through-real-world-phenomena-and-analogies-lucas-kaldstrom
youtube_search_url: https://www.youtube.com/results?search_query=Understanding+Kubernetes+Through+Real-World+Phenomena+and+Analogies+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Understanding Kubernetes Through Real-World Phenomena and Analogies - Lucas Käldström

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Lucas Käldström
- Schedule: https://kccnceu2022.sched.com/event/ytr4/understanding-kubernetes-through-real-world-phenomena-and-analogies-lucas-kaldstrom
- Busca YouTube: https://www.youtube.com/results?search_query=Understanding+Kubernetes+Through+Real-World+Phenomena+and+Analogies+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Understanding Kubernetes Through Real-World Phenomena and Analogies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytr4/understanding-kubernetes-through-real-world-phenomena-and-analogies-lucas-kaldstrom
- YouTube search: https://www.youtube.com/results?search_query=Understanding+Kubernetes+Through+Real-World+Phenomena+and+Analogies+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GpJz-Ab8R9M
- YouTube title: Understanding Kubernetes Through Real-World Phenomena and Analogies - Lucas Käldström
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/understanding-kubernetes-through-real-world-phenomena-and-analogies/GpJz-Ab8R9M.txt
- Transcript chars: 27791
- Keywords: actually, complexity, systems, google, exactly, randomness, conductor, control, server, desired, everything, whatever, declarative, entropy, action, theory, necessary, servers

### Resumo baseado na transcript

hi yeah can you hear me perfect um well thanks for the introduction thanks for attending this this talk i'm really excited to share these kind of ideas with you today um we're gonna walk through really the why of what we're doing so it's going to be a little bit philosophical a little bit kind of hopefully maybe even new ideas and kind of get your head spinning after this that's that's the kind of idea so no it's a little bit delay uh i'm lucas trustrum studying at we don't ssh into them anymore we don't run commands at a certain server directly we just tell that what is the end state what is the key goal of the system this will change over time as new security vulnerabilities come out and new

### Excerpt da transcript

hi yeah can you hear me perfect um well thanks for the introduction thanks for attending this this talk i'm really excited to share these kind of ideas with you today um we're gonna walk through really the why of what we're doing so it's going to be a little bit philosophical a little bit kind of hopefully maybe even new ideas and kind of get your head spinning after this that's that's the kind of idea so no it's a little bit delay uh i'm lucas trustrum studying at uh alto university at the moment but i've already been doing some quite some different things in in the kubernetes community starting from kubernetes and arm which is also my my twitter username if you want to tweet tweet at me and give feedback i'm definitely looking for feedback for this currently i'm i'm kind of looking into these these kind of kubernetes research things that that's why why do we do what we do and how can we kind of continue and sustain the the kind of development of the community by going back to first principles right so but also been doing cube adm and some other interesting upstream maintenance work in the past few years but um yes let's take a look at the y and um when we're coming to this kubecon conference we get a lot of the watts so we get a lot of the yaml a lot of the kind of run this command you know in this order and then write this script here and it's going to do its thing or like click this button but then we might ask how so so how does it work well when you submit a port when you submit some application to kubernetes it's going to schedule the different things to the different nodes in a certain order that we also have a lot of talks about but now i want to go even more to the core and wonder why did we choose different certain patterns that we now have kind of as de facto standards in the kubernetes community so this is kind of what i don't want to happen so if we if we don't look at why we're doing things uh we might end up missing the kind of problem we're solving so there's two kinds of of complexities and i thank joe bida for this uh this analogy so there's necessary complexity and that's the one we're going to look into today and there's also kind of accidental complexity and and the accidental complexity we hope to remove over time so that users aren't annoyed in just vain but the necessary complexity is actually there because of reason and we're going to go into the reason what is the reason what is the necessary complexity we might not even know tha
