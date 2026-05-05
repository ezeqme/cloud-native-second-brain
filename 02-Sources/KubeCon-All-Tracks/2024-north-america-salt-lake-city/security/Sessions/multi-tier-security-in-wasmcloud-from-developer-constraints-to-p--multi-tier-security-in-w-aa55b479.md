---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security", "Platform Engineering", "Runtime Containers"]
speakers: ["Brooks Townsend", "Cosmonic"]
sched_url: https://kccncna2024.sched.com/event/1i7pL/multi-tier-security-in-wasmcloud-from-developer-constraints-to-platform-extensibility-brooks-townsend-cosmonic
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Tier+Security+in+WasmCloud%3A+From+Developer+Constraints+to+Platform+Extensibility+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Multi-Tier Security in WasmCloud: From Developer Constraints to Platform Extensibility - Brooks Townsend, Cosmonic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Platform Engineering]], [[Runtime Containers]]
- País/cidade: United States / Salt Lake City
- Speakers: Brooks Townsend, Cosmonic
- Schedule: https://kccncna2024.sched.com/event/1i7pL/multi-tier-security-in-wasmcloud-from-developer-constraints-to-platform-extensibility-brooks-townsend-cosmonic
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Tier+Security+in+WasmCloud%3A+From+Developer+Constraints+to+Platform+Extensibility+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Multi-Tier Security in WasmCloud: From Developer Constraints to Platform Extensibility.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pL/multi-tier-security-in-wasmcloud-from-developer-constraints-to-platform-extensibility-brooks-townsend-cosmonic
- YouTube search: https://www.youtube.com/results?search_query=Multi-Tier+Security+in+WasmCloud%3A+From+Developer+Constraints+to+Platform+Extensibility+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tdr_daxJd28
- YouTube title: Multi-Tier Security in WasmCloud: From Developer Constraints to Platform Extensibility - B. Townsend
- Match score: 1.019
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/multi-tier-security-in-wasmcloud-from-developer-constraints-to-platfor/tdr_daxJd28.txt
- Transcript chars: 37129
- Keywords: actually, assembly, application, component, platform, runtime, wasm, secrets, secret, security, binary, little, capabilities, capability, running, source, implementation, policy

### Resumo baseado na transcript

so thank you all for so much for coming uh today we're going to be talking about multi-tier Security in wasm cloud from developer constraints to P platform extensibility so my name is Brooks Townsen I'm a senior software engineer at cosonic and I've been a maintainer of the wasm cloud project since it started in late 2019 it's been in the cncf since 2021 uh and just recently we hit incubating which was a huge milestone for for us as a project I'm a rust station I'm a demo at runtime with the web assembly sandbox so this was a further demonstration of what we can do with w cloud and I think it's really important to note that uh you know as we as we look at the demo takeaways this capability driven

### Excerpt da transcript

so thank you all for so much for coming uh today we're going to be talking about multi-tier Security in wasm cloud from developer constraints to P platform extensibility so my name is Brooks Townsen I'm a senior software engineer at cosonic and I've been a maintainer of the wasm cloud project since it started in late 2019 it's been in the cncf since 2021 uh and just recently we hit incubating which was a huge milestone for for us as a project I'm a rust station I'm a demo enthusiast you can see me up there probably wearing the same t-shirt that I'm wearing right now preparing to do more demos so very excited about that and uh I'm a developer and the reason why I call that out explicitly is because when I started my career I was working at Capital One and I was actually provisioning kubernetes clusters for like our internal developer platform so I've gone everywhere from like running QB ADM on an ec2 instance to writing the code that runs on that kubernetes instance and so I hope that that kind of gives some context between what I'm talking about when I talk about platform engineers and developers CU I've kind of been on both sides of that fence so what we're going to go through in the talk today we're going to talk about open source security for platforms the problem that we have uh I'm going to go through a little introduction on wasm cloud a show of hands how many of you have heard of the wasm cloud project all right well that's like uh you know good bit of the room it's nice uh how many of you have heard of web assembly before okay so even more great so we got a great audience for this we're going to go through that introduction it's not going to take too long and then we're just going to jump into rapid fire demos back and forth with uh talking about wasm Cloud's multi-tier security model and then the Innovation that we had earlier this year in the wasm cloud secrets and the extensibility there so you'll see everything happening uh it should be should be a lot of fun so let's start out with the fun quote 74% of code-based uh this was a a study in 2024 contained highrisk open source vulnerabilities not like a vulnerability like that would be bad high-risk open- Source vulnerabilities and this really puts a high burden on the developers deploying applications whether it's on their own or internal uh to a big Enterprise to keep their code up to date it the the idea of coming from open- Source vulnerabilities means that these are libraries you're importing
