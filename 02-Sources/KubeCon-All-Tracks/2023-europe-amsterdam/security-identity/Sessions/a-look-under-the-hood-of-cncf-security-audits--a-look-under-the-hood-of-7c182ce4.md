---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Adam Korczynski", "David Korczynski", "Ada Logics"]
sched_url: https://kccnceu2023.sched.com/event/1Hybf/a-look-under-the-hood-of-cncf-security-audits-adam-korczynski-david-korczynski-ada-logics
youtube_search_url: https://www.youtube.com/results?search_query=A+Look+Under+the+Hood+of+CNCF+Security+Audits+CNCF+KubeCon+2023
slides: []
status: parsed
---

# A Look Under the Hood of CNCF Security Audits - Adam Korczynski & David Korczynski, Ada Logics

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Adam Korczynski, David Korczynski, Ada Logics
- Schedule: https://kccnceu2023.sched.com/event/1Hybf/a-look-under-the-hood-of-cncf-security-audits-adam-korczynski-david-korczynski-ada-logics
- Busca YouTube: https://www.youtube.com/results?search_query=A+Look+Under+the+Hood+of+CNCF+Security+Audits+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre A Look Under the Hood of CNCF Security Audits.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hybf/a-look-under-the-hood-of-cncf-security-audits-adam-korczynski-david-korczynski-ada-logics
- YouTube search: https://www.youtube.com/results?search_query=A+Look+Under+the+Hood+of+CNCF+Security+Audits+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YGN0Z9SOVBE
- YouTube title: A Look Under the Hood of CNCF Security Audits - Adam Korczynski & David Korczynski, Ada Logics
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/a-look-under-the-hood-of-cncf-security-audits/YGN0Z9SOVBE.txt
- Transcript chars: 23843
- Keywords: security, issues, projects, whether, audits, report, source, usually, threat, process, consider, product, audience, maintainers, deploy, little, reports, vulnerabilities

### Resumo baseado na transcript

hello everyone thank you very much for coming to our talk this is a look under the hood of cncf security audits my name is Adam kochinski and I'm giving this a talk together with David kojinski this is the agenda for our talk we will go through what the cncf security audits are the internal mechanics of the audits some insights and results and outcomes from six security audits that we have carried out and how the community can get involved in the ongoing security work you may have

### Excerpt da transcript

hello everyone thank you very much for coming to our talk this is a look under the hood of cncf security audits my name is Adam kochinski and I'm giving this a talk together with David kojinski this is the agenda for our talk we will go through what the cncf security audits are the internal mechanics of the audits some insights and results and outcomes from six security audits that we have carried out and how the community can get involved in the ongoing security work you may have seen stuff like this on Twitter or the cncfs on block or a project a cncf projects blog as well and in this talk we go through the work that goes into getting to this place where we announced the findings and we wrap up the security audit so the projects that we we have audited over the last year so this will be a talk about six audits we've done throughout the last year maybe a little bit more than last year and these are the projects Argo psyllium cryo istio cup Edge and flux so we will mainly be speaking out of these sometimes we will generalize to a bit more audits because there's more sensitive security audience going on and there will also be some insights about that so uh the position of see if since you have security audits into those that we talk about now is first and foremost they are made available by the cncf itself and then also the open source technology Improvement fund and both of these organizations help commission the Audits and facilitate them help some of the communication with the retainers and and all sorts of things that are necessary to carry out these audience so thanks a lot to both of these organizations and in a sense because both of the organizations that get this work sort of started it is like a goal is in that sense becomes we want to make open source security audits that means a lot of the things that happens in the audit are in fact open to for everyone to see and it's an ongoing effort there are some links to some blog posts that summarize audits of a lot more projects than just these six months and this is also just the security audits that we present here are also just a small part of the whole engagement that since you have those in terms of securing the cncf landscape other things include uh security automation by way of fussing and we included a small blog post here which summarizes a lot of the the results from that so what is that since since you have security audit it's kind of it's a time-boxed engagement although it's a bit flexible s
