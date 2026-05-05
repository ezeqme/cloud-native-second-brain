---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Rita Zhang", "Jeremy Rickard", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1hoxr/working-together-to-improve-security-visibility-in-kubernetes-rita-zhang-jeremy-rickard-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Working+Together+to+Improve+Security+Visibility+in+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Working Together to Improve Security Visibility in Kubernetes - Rita Zhang & Jeremy Rickard, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Rita Zhang, Jeremy Rickard, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1hoxr/working-together-to-improve-security-visibility-in-kubernetes-rita-zhang-jeremy-rickard-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Working+Together+to+Improve+Security+Visibility+in+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Working Together to Improve Security Visibility in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxr/working-together-to-improve-security-visibility-in-kubernetes-rita-zhang-jeremy-rickard-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Working+Together+to+Improve+Security+Visibility+in+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=f-NJptXlp5I
- YouTube title: Working Together to Improve Security Visibility in Kubernetes - Rita Zhang & Jeremy Rickard
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/working-together-to-improve-security-visibility-in-kubernetes/f-NJptXlp5I.txt
- Transcript chars: 28357
- Keywords: actually, release, security, process, scanners, issues, obviously, please, pretty, information, important, vulnerabilities, report, vulnerability, database, releases, specifically, hacker

### Resumo baseado na transcript

uh thanks for coming to uh working together to improve security visibility in kubernetes my name is Jeremy Rickard I'm a co-chair of Sig release uh and an engineer at Microsoft uh my my name is Rita I am part of the kubernetes security response committee also SE goth also Microsoft all right um so thank you for being here on a Friday uh I know it's been a really long conference but thank you for being here and you must really care about security if you're in this talk Sig that spe specifically looks at uh protecting access and control of kubernetes apis uh specifically you know authentication authorization are part of it as well um and also the Sig looks at auditing as well as security policies uh and then it's also um also has sub projects within the authent uh within the S off space and they often get uh consulted on uh issues that that um uh people report on okay next up we have Sig security Sig security is a interesting Sig they don't own specific features inside of kubernetes but they handle things like regular security audits um they helped build this thing called the official cve feed which is a great place where you can go and see all the cves as they as they happen and are released uh and they work on Cross cutting security documentation and working across the sigs to help maintain uh the community's security posture uh so let's maybe talk about what what is a life...

### Excerpt da transcript

uh thanks for coming to uh working together to improve security visibility in kubernetes my name is Jeremy Rickard I'm a co-chair of Sig release uh and an engineer at Microsoft uh my my name is Rita I am part of the kubernetes security response committee also SE goth also Microsoft all right um so thank you for being here on a Friday uh I know it's been a really long conference but thank you for being here and you must really care about security if you're in this talk so I just want to thank everybody um but also the most important thing that you probably could get out of this talk is if you see a security problem please please please work with us and don't disclose it publicly right the reason why we have a security response committee um and bunch of really nice Sig maintain uh project maintainers is we want to work with you to address these uh vulnerabilities privately right and make sure we can get all of them patched before the B guys get to them so if there's anything you take out of the session is please report it in with those um emails as well as um the website uh if you want to also get bounties for them okay so we're going to start off by talking about how sigs work together to help achieve security for the project and provide visibility into that whenever a vulnerability is disclosed the SRC is going to work with a bunch of other sigs to help fix those things Sig release will help cut releases Sig security is going to help with some tooling to help visualize some of those things so we're going to dive into each one of these areas and figure out exactly what they do oh I cannot see um okay sorry all right first off um let's just talk about a few of the uh sigs and committees that are formed uh within the project to specifically address cves um so first we start with SRC security response committee it's a commit it's not a Sig it is responsible for triaging and fixed coordinations uh and it it is also responsible for disclosing the security issues in kubernetes uh the the SRC the kubernetes SRC is a CNA uh which stands for cve naming Authority uh it basically authorizes these uh folks to actually issue a cve and report it to uh the the national vulnerability database um currently we have eight representatives from various companies uh and with diverse experience in kubernetes um and our job is again ensuring that um there are different areas of cetes and the ecosystems on top of cetes are well represented right and we also want to make sure um tha
