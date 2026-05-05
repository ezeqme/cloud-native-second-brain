---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Pushkar Joglekar", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV48/keeping-up-with-the-cves-how-to-find-a-needle-in-a-haystack-pushkar-joglekar-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Keeping+Up+with+the+CVEs%3A+How+to+Find+a+Needle+in+a+Haystack%3F+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Keeping Up with the CVEs: How to Find a Needle in a Haystack? - Pushkar Joglekar, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Los Angeles
- Speakers: Pushkar Joglekar, VMware
- Schedule: https://kccncna2021.sched.com/event/lV48/keeping-up-with-the-cves-how-to-find-a-needle-in-a-haystack-pushkar-joglekar-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Keeping+Up+with+the+CVEs%3A+How+to+Find+a+Needle+in+a+Haystack%3F+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Keeping Up with the CVEs: How to Find a Needle in a Haystack?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV48/keeping-up-with-the-cves-how-to-find-a-needle-in-a-haystack-pushkar-joglekar-vmware
- YouTube search: https://www.youtube.com/results?search_query=Keeping+Up+with+the+CVEs%3A+How+to+Find+a+Needle+in+a+Haystack%3F+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2cvWmY4xvLU
- YouTube title: Keeping Up with the CVEs: How to Find a Needle in a Haystack? - Pushkar Joglekar, VMware
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/keeping-up-with-the-cves-how-to-find-a-needle-in-a-haystack/2cvWmY4xvLU.txt
- Transcript chars: 27150
- Keywords: images, vulnerabilities, actually, vulnerability, container, security, essentially, application, debian, question, another, whether, release, scanner, impact, threat, number, production

### Resumo baseado na transcript

hello uh welcome to keeping with the suvs how to find a needle in a haystack there will be q a uh at the end of this presentation please raise your hand if you are in person and would like to ask a question after the session don't forget to rate the session on sketch.com and now please welcome pushkar our senior security engineer at vmware thank you thank you colleen can everyone hear me fine all right cool so thank you first of all for coming here instead of

### Excerpt da transcript

hello uh welcome to keeping with the suvs how to find a needle in a haystack there will be q a uh at the end of this presentation please raise your hand if you are in person and would like to ask a question after the session don't forget to rate the session on sketch.com and now please welcome pushkar our senior security engineer at vmware thank you thank you colleen can everyone hear me fine all right cool so thank you first of all for coming here instead of going to the attendee party and also one question i have for all of you is how many of you are kubernetes end users and how many of you are work for companies that ship kubernetes or you or are related to kubernetes so good news is the talk is going to be helpful for both of you so let's see let's start a little bit about me i'm a senior security engineer at vmware tanzu was born and brought up in india then moved here for studies and been working here for a while i worked in visa as an end user and now i work for vmware tanzu i started working on kubernetes for a few years now and went so deep into it that was able to write couple of chapters for nigel porton's kubernetes book i i speak different languages so if anyone is virtual and wants to ask a different question in a different language that's fine as well i i am generally more available on twitter than linkedin so if you want to reach me that's probably your best bet all right let's get on with it so the main question here is why is this graph looking like the way it looks and the if you see pretty much more or less there is a gradual curve of vulnerabilities going upward every year since last 20 22 years this year there are still about two and a half months left so there is a chance that it might exceed the count in 2020 now this is an objective metric the reasons behind why number of vulnerabilities are more that's probably a discussion for another talk but we also asked our cncf end users as part of tax security work and we ask them what do you do to secure your kubernetes and container environments what they responded with is we do image scanning and i felt okay great so that means they are managing vulnerabilities really well but we asked another question to them and they said managing vulnerabilities is our one of the top most concerns so that kind of doesn't make sense to me where if you're doing image scanning the obvious conclusion would be maybe you're doing well with managing vulnerabilities so the question again is what's really goin
