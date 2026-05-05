---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["AI ML", "Security"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW9x/open-policy-agent-opa-thats-one-small-bump-for-opa-but-one-giant-leap-for-policy-as-code-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29%3A+That%27s+One+Small+Bump+for+OPA%2C+but+One+Giant+Leap+for+Policy+as+Code+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Open Policy Agent (OPA): That's One Small Bump for OPA, but One Giant Leap for Policy as Code | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW9x/open-policy-agent-opa-thats-one-small-bump-for-opa-but-one-giant-leap-for-policy-as-code-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29%3A+That%27s+One+Small+Bump+for+OPA%2C+but+One+Giant+Leap+for+Policy+as+Code+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Open Policy Agent (OPA): That's One Small Bump for OPA, but One Giant Leap for Policy as Code | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9x/open-policy-agent-opa-thats-one-small-bump-for-opa-but-one-giant-leap-for-policy-as-code-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Open+Policy+Agent+%28OPA%29%3A+That%27s+One+Small+Bump+for+OPA%2C+but+One+Giant+Leap+for+Policy+as+Code+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=48sDVk5vdKU
- YouTube title: Open Policy Agent (OPA): That's One Small Bump for OPA, but One Giant Leap for Policy as Code | PLT
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/open-policy-agent-opa-thats-one-small-bump-for-opa-but-one-giant-leap/48sDVk5vdKU.txt
- Transcript chars: 4966
- Keywords: policy, application, hopefully, working, familiar, within, benefits, allows, recommend, already, applications, managing, certain, cluster, deploy, policies, business, language

### Resumo baseado na transcript

looks like it's working hello everybody um my name is Charlie I work at styra on the developer relations team and on the OPA project open policy agent project um Opa has been graduated for quite some time now since the beginning of 2021 so many of you here today will have heard of it already um but for those of you who haven't you've likely come up against uh something that we call policy so policy is any rule um or enforcement that you want to enforce in your

### Excerpt da transcript

looks like it's working hello everybody um my name is Charlie I work at styra on the developer relations team and on the OPA project open policy agent project um Opa has been graduated for quite some time now since the beginning of 2021 so many of you here today will have heard of it already um but for those of you who haven't you've likely come up against uh something that we call policy so policy is any rule um or enforcement that you want to enforce in your applications or in the platforms that you're uh that you're managing so for example in an application it might be common to have a role where admins are only allowed uh to do certain actions within that application and or in a cluster you you might um put controls on who can deploy into which name spaces or can deploy certain types of resources so hopefully these kinds of policies are uh hopefully familiar to you but policy is uh you know much broader than just what can happen in an application any one application in any one kubernetes cluster policy is everywhere policy is uh the business rules that that make organizations work and the problem the problem that this poses is that when policy is defined in many different systems and using often unstructured language or varying implementations in different uh where it's in forced in different places uh this this creates uh creates challenges inconsistencies and insecurity uh we can do better than that and that's where open policy agent comes in so Opa gives you a consistent way to express your policy um to offload policy evaluation and manage that policy's life cycle for any use case so whether that's an business application that you're working on or a platform that you're in charge of managing you can integrate with Opa to define the policies the policy rules that you need U to to to ensure are withheld within that environment or within that application you can offload that to Opa um the language is designed especially to be useful and expressive for policy use cases uh I'll show a short example in one second um but I think also what's often missed about Opa is the the apis that we offer for um for reloading of policy without redeploying all your applications or redeploying your platform as well as sending audit data about the policy decisions which it's made um so yeah uh Opa helps you do policy but as code and hopefully we're at ccon people are familiar with infrastructure as code uh various other things as code hopefully the benefits of the doing d
