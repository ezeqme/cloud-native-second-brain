---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Harsh Thakur", "Civo"]
sched_url: https://kccncna2021.sched.com/event/lUzd/unraveling-the-mystery-of-versioning-crds-harsh-thakur-civo
youtube_search_url: https://www.youtube.com/results?search_query=Unraveling+the+Mystery+of+Versioning+CRDs+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Unraveling the Mystery of Versioning CRDs - Harsh Thakur, Civo

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: United States / Los Angeles
- Speakers: Harsh Thakur, Civo
- Schedule: https://kccncna2021.sched.com/event/lUzd/unraveling-the-mystery-of-versioning-crds-harsh-thakur-civo
- Busca YouTube: https://www.youtube.com/results?search_query=Unraveling+the+Mystery+of+Versioning+CRDs+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Unraveling the Mystery of Versioning CRDs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzd/unraveling-the-mystery-of-versioning-crds-harsh-thakur-civo
- YouTube search: https://www.youtube.com/results?search_query=Unraveling+the+Mystery+of+Versioning+CRDs+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vZkl9KocroY
- YouTube title: Unraveling the Mystery of Versioning CRDs - Harsh Thakur, Civo
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/unraveling-the-mystery-of-versioning-crds/vZkl9KocroY.txt
- Transcript chars: 10214
- Keywords: version, conversion, storage, stored, objects, object, versioning, versions, convert, functions, builder, served, always, change, existing, fields, package, create

### Resumo baseado na transcript

hello everyone my name is harsh and today i'll be talking about city version little bit about me i'm a developer civil cloud which is a blazingly fast managed humanities provider i'm also maintainer at open ebs which is the cncf sandbox storage project i'm also a hashicorp ambassador and i really love playing chess so getting right into it cid versioning is a lot like any other api versioning conventions so you typically do not want to add a required field in the same version or change the name

### Excerpt da transcript

hello everyone my name is harsh and today i'll be talking about city version little bit about me i'm a developer civil cloud which is a blazingly fast managed humanities provider i'm also maintainer at open ebs which is the cncf sandbox storage project i'm also a hashicorp ambassador and i really love playing chess so getting right into it cid versioning is a lot like any other api versioning conventions so you typically do not want to add a required field in the same version or change the name and types of the existing fields because that would break the end user specs and the reasons for wanting to change names and types of fields are to simplify user inputs for better validations or simply because you want to evolve to the new api conventions for example uh kubernetes sub resource status has evolved from using faces to using conditions there are times when you don't really need to upgrade as well and that's when you want to add optional fields as that would wouldn't break the end user specs and uh change validations and by that i mean validations which don't break the existing defaults of the specs so when it comes to cid versioning there are two views for it as an end user we are always exposed to the server version and server versions can be more than one whereas the stored version is what's really stored uh in hcd and it can only be one so the api can read the stored version uh from at cd and represent it in multiple versions to us and we look at how it does that but essentially all you need to know is that store version can always only be one so when it comes to conversion strategy there are two of them the first one is really a last mile change where you want to just bump up the api version and there are no schema changes in your uh crds the second one is what we really uh think about when we think about convert conversion strategy and we look at uh how it works so i have a little demo and in this demo i'll have two versions of v1 and v2 and in the beginning v1 would be the stored version and when user requests v2 uh view of the object what happens is the api reads the object from at cd in v1 it has a conversion web book which we have written and i'll show that in a moment but the conversion workbook would then throw back the object to api in v2 as it has some conversion functions and the api then returns back uh output to the user now what i've done is i've scaffolded this project using cube builder i even played along with the basic example of gu
