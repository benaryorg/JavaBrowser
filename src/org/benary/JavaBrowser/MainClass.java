/*
 * The MIT License
 *
 * Copyright 2014 benaryorg.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package org.benary.JavaBrowser;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;

/**
 *
 * @author benaryorg
 */
public class MainClass
{

	public static void main(String[] args) throws IOException
	{
		Socket s=new Socket(InetAddress.getByName("localhost"),80);
		System.out.println(s.getInetAddress().getHostName()+":"+s.getPort());
		BufferedWriter w=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
		BufferedReader r=new BufferedReader(new InputStreamReader(s.getInputStream()));
		String line;
		w.append(
			"GET / HTTP/1.1\n"
			+"Host: localhost\n"
			+"\n"
		);
		w.flush();
		while(!r.ready())
		{
			System.out.println("Not Ready!");
		}
		while((line=r.readLine())!=null)
		{
			System.out.println(line);
		}
		w.close();
		r.close();
	}
}
