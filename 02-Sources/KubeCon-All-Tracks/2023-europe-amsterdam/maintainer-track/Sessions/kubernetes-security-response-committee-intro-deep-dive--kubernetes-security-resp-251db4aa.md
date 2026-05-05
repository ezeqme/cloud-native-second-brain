---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Monis Khan", "Microsoft", "Micah Hausler", "AWS"]
sched_url: https://kccnceu2023.sched.com/event/1HyRw/kubernetes-security-response-committee-intro-deep-dive-monis-khan-microsoft-micah-hausler-aws
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Security+Response+Committee%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes Security Response Committee: Intro & Deep Dive - Monis Khan, Microsoft & Micah Hausler, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Monis Khan, Microsoft, Micah Hausler, AWS
- Schedule: https://kccnceu2023.sched.com/event/1HyRw/kubernetes-security-response-committee-intro-deep-dive-monis-khan-microsoft-micah-hausler-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Security+Response+Committee%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes Security Response Committee: Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyRw/kubernetes-security-response-committee-intro-deep-dive-monis-khan-microsoft-micah-hausler-aws
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Security+Response+Committee%3A+Intro+%26+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=re7HBYUYCB8
- YouTube title: Kubernetes Security Response Committee: Intro & Deep Dive - Monis Khan, Microsoft & Micah Hausler
- Match score: 0.835
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-security-response-committee-intro-deep-dive/re7HBYUYCB8.txt
- Transcript chars: 30530
- Keywords: security, report, committee, bounty, please, hacker, critical, sometimes, process, issues, generally, public, distributors, vendor, anything, github, account, release

### Resumo baseado na transcript

all right thanks everyone for coming um yeah you are if you're here to talk and or listen um about the uh kubernetes security committee you're in the right place um I'm Micah housler I'm a principal engineer at AWS I uh focused on kubernetes security ecas security um hi y'all I'm at Microsoft I'm Mo uh let's see I guess I've been doing kubernetes stuff since 2016 now and all sorts of security stuff so thank you for coming so before we we start our talk we we'd say

### Excerpt da transcript

all right thanks everyone for coming um yeah you are if you're here to talk and or listen um about the uh kubernetes security committee you're in the right place um I'm Micah housler I'm a principal engineer at AWS I uh focused on kubernetes security ecas security um hi y'all I'm at Microsoft I'm Mo uh let's see I guess I've been doing kubernetes stuff since 2016 now and all sorts of security stuff so thank you for coming so before we we start our talk we we'd say um we wanted to say if you think you found an issue um stop uh before you you tell somebody uh the first place you need to go is the kubernetes uh dot IO Security on that page you'll see a bunch of helpful resources on what to do if you think you found one um the the short version for for this talk is please please don't post anything that you think is or might be a security issue on GitHub or kubernetes slack or message it to someone you think is on the security committee um on slack uh usernames are are can be semi uh faked yep so please report to uh our hacker one bug Bounty program um or to our just our inbox security at kubernetes.io so go ahead so what does the like SRC do so we run the hacker one bug Bounty so if you're a security researcher and that's how you make your living um you know we're happy to give you money if you come tell us where we screwed up we're more than happy to do that uh but also like a large part of our work is just coordinating with the various code owners to get fixes out so while we have a lot of expertise within the group we don't know everything about Cube so a lot of times we're spending a decent chunk of our effort just saying like hey Sig leads is this an issue is this how it's supposed to work is this a doc fix like what is this how severe it is who does it impact those kind of things so we have a pretty bad broad representation within the community so like myself and Rita or Microsoft Mica and biology are from Amazon Joel's from Red Hat CJ's from Google so this diversity is really important to us because what might matter to Microsoft might not matter to Amazon depending on how you deploy and run kubernetes but we want to make sure that when we do a severity rating we're taking into account various deployment models within the community and just taking great care we want to be on the side of caution right so like if we can think of like a subset of individuals where something that we might consider a medium is a high for them so we want to take those types
