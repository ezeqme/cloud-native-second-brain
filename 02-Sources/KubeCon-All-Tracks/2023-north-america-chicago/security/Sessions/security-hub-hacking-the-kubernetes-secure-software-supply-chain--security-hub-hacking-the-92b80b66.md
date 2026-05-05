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
themes: ["AI ML", "Security", "Kubernetes Core"]
speakers: ["John McBride", "Opensauced", "Sean McGinnis", "AWS"]
sched_url: https://kccncna2023.sched.com/event/1SKZK/security-hub-hacking-the-kubernetes-secure-software-supply-chain-with-zip-domains-john-mcbride-opensauced-sean-mcginnis-aws
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+Hacking+the+Kubernetes+Secure+Software+Supply-chain+with+.zip+Domains+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SECURITY HUB: Hacking the Kubernetes Secure Software Supply-chain with .zip Domains - John McBride, Opensauced & Sean McGinnis, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: John McBride, Opensauced, Sean McGinnis, AWS
- Schedule: https://kccncna2023.sched.com/event/1SKZK/security-hub-hacking-the-kubernetes-secure-software-supply-chain-with-zip-domains-john-mcbride-opensauced-sean-mcginnis-aws
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+Hacking+the+Kubernetes+Secure+Software+Supply-chain+with+.zip+Domains+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SECURITY HUB: Hacking the Kubernetes Secure Software Supply-chain with .zip Domains.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1SKZK/security-hub-hacking-the-kubernetes-secure-software-supply-chain-with-zip-domains-john-mcbride-opensauced-sean-mcginnis-aws
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+Hacking+the+Kubernetes+Secure+Software+Supply-chain+with+.zip+Domains+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=57k-KwOsj9c
- YouTube title: SECURITY HUB: Hacking the Kubernetes Secure Software Supply-chain wi... John McBride & Sean McGinnis
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-hub-hacking-the-kubernetes-secure-software-supply-chain-with/57k-KwOsj9c.txt
- Transcript chars: 20459
- Keywords: actually, website, software, download, domains, getting, signature, malicious, github, coming, question, little, social, engineering, probably, domain, internet, looking

### Resumo baseado na transcript

my name is John and I'm Sean there we go uh and this is hacking the kubernetes software supply chain with zip domains uh so in this talk kind of what we want to present is uh a little bit of background about zip domains the trouble they may cause uh the the role of social engineering in that uh a little bit of a demo and then the the uh the defense against something like that as well so uh before we get too much further let's go into

### Excerpt da transcript

my name is John and I'm Sean there we go uh and this is hacking the kubernetes software supply chain with zip domains uh so in this talk kind of what we want to present is uh a little bit of background about zip domains the trouble they may cause uh the the role of social engineering in that uh a little bit of a demo and then the the uh the defense against something like that as well so uh before we get too much further let's go into a little bit of background on what zip domains are uh how I somehow found myself with the kubernetes doz uh website uh and then get into a demo so uh ZIP domains or top level domains became available in May of this year and generally to kind of the out outcry of the internet people people generally just said like this is is this is probably just bad for the safety of The Wider internet having a top level domain like Johns Cool website. zip or Sean's cool website. zip or something more nefarious like my files.zip or kubernetes dzip uh just gives you kind of the air of like oh is it a website is it a zip file with a bunch of stuff in it um who knows at this point dotzip top level domains are out there so I got it in my head that oh like who has kubernetes doz like somebody picked it up already and this was like months later at this point uh and I was able to get it for like $12 uh and the first thing I did was immediately redirected to kubernetes doio I talked with dims a little bit and we just made sure that like okay like we don't want this like out in the wild uh I can only imagine the kind of things people would do with uh some nefarious actor saying hey I can you help me figure out what's wrong with my cluster here are my logs kubernetes dzip can you help me right um yeah so dotzip top level domains websites probably probably not a good idea for just the general safety of the internet uh but let's break down how a malicious actor would use social engineering azip top level domain uh and and some tricks uh with a malicious URL to make this a much much worse kind of attack um so a quick show of hands uh who thinks that this URL goes to Google go.com nobody wow uh who thinks it goes to bing.com a few people yes you would be correct uh so let's break this down real quick the first part htps that's the protocol the next part before the at sign is essentially a login like a username login to this website and then bing.com is where that would be directed uh let's do this again but with a more malicious looking URL again we have ht
