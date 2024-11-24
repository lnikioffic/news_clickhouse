import type Tag from "@/models/Tag";
import type TagBase from "@/models/TagBase";
import axios from "axios";

const SERVER_URL = '/api/tags'


export async function createTag(tag: TagBase): Promise<Tag> {
    const { data } = await axios.post(SERVER_URL, tag)
    return data
}

export async function getTags(): Promise<Array<Tag>> {
    const { data } = await axios.get(SERVER_URL)
    return data
}