---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: []
sched_url: https://kccncna2023.sched.com/event/1VDnW/security-hub-unconference-gittuf-a-security-layer-for-git-repositories
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+gittuf%3A+A+Security+Layer+for+Git+Repositories+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SECURITY HUB UNCONFERENCE: gittuf: A Security Layer for Git Repositories

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: N/A
- Schedule: https://kccncna2023.sched.com/event/1VDnW/security-hub-unconference-gittuf-a-security-layer-for-git-repositories
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+gittuf%3A+A+Security+Layer+for+Git+Repositories+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SECURITY HUB UNCONFERENCE: gittuf: A Security Layer for Git Repositories.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1VDnW/security-hub-unconference-gittuf-a-security-layer-for-git-repositories
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB+UNCONFERENCE%3A+gittuf%3A+A+Security+Layer+for+Git+Repositories+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=f5uSRKTIQfk
- YouTube title: SECURITY HUB UNCONFERENCE: gittuf, A Security Layer for Git Repositories
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-hub-unconference-gittuf-a-security-layer-for-git-repositories/f5uSRKTIQfk.txt
- Transcript chars: 24076
- Keywords: repository, policy, branch, security, source, actually, policies, change, github, signing, around, verify, commits, developer, itself, semantics, support, someone

### Resumo baseado na transcript

as Mar said I'm AA I'm a PhD student at NYU I research software supply chain security here in the cncf I'm one of the maintainers of int Toto and for about a year just over a year now we've been building K uh for securing get repositories so you know uh just to get just to you know lay out the land a bit the state of git Security today is uh git is cored addressed so you get some Integrity checks out of the box it also has

### Excerpt da transcript

as Mar said I'm AA I'm a PhD student at NYU I research software supply chain security here in the cncf I'm one of the maintainers of int Toto and for about a year just over a year now we've been building K uh for securing get repositories so you know uh just to get just to you know lay out the land a bit the state of git Security today is uh git is cored addressed so you get some Integrity checks out of the box it also has some semantics for things like signing your commits and tags and pushes to but setting that aside for now uh it if if you looked at a best practice guide for Source control uh source code Management Systems in the last few years you probably come across this thing that says you should sign your commits and things like that and you know K does that offer allows you to do that out of the box but uh what G does not support is uh actually defining policy polies around all of these things it's like uh if I'm supposed to be signing my commits and so on what like as a verifier as someone who's actually going to going to verify those signatures how do they know what keys to trust for that repository and uh when should they stop trusting a key for that repository maybe the key was lost or maybe the developer stopped working on the project and they no longer considered a maintainer you know that keeps happening uh other access control is things like oh uh what kind of actions can a developer take in a repository like are they allowed to merge something into the main branch typically not that's typically a uh capability you limit to a handful of maintainers and so on or uh what kind of which which of which files a developer can write to or conversely not write to things like that uh which is just not supported in G repositories so that's that's these are the kind of questions we started out with and that's where uh I'm going to present to you you know giu so one of the first things we started doing in getu is to try and see how we could store policies around all of the these kinds of you know to to try and answer and to try and uh enforce those kinds of checks in a g repository within a repository itself uh we uh get allows you to store things in custom namespaces which is really really neat and we take advantage of that quite a bit uh so we encode policies using some semantics from the update framework a graduated project here at the cncf which you might have heard of a bit in the last few days especially as well as some uh semantics from the inta
